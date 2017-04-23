#Renyi entanglement entropy of Bose-Hubbard chains in 1D.

push!(LOAD_PATH, joinpath(dirname(@__FILE__), "src"))

using BoseHubbardDiagonalize
using ArgParse
using JeszenszkiBasis

s = ArgParseSettings()
s.autofix_names = true
@add_arg_table s begin
    "M"
        help = "number of sites"
        arg_type = Int
        required = true
    "N"
        help = "number of particles"
        arg_type = Int
        required = true
    "--out"
        metavar = "FILE"
        help = "path to output file"
        required = true
    "--site-max"
        metavar = "N"
        help = "site occupation restriction"
        arg_type = Int
end

add_arg_group(s, "boundary conditions")
@add_arg_table s begin
    "--pbc"
        help = "periodic boundary conditions (default)"
        arg_type = BdryCond
        action = :store_const
        dest_name = "boundary"
        constant = PBC
        default = PBC
    "--obc"
        help = "open boundary conditions"
        arg_type = BdryCond
        action = :store_const
        dest_name = "boundary"
        constant = OBC
        default = PBC
end

add_arg_group(s, "BH parameters")
@add_arg_table s begin
    "--u-min"
        metavar = "U"
        help = "minimum U"
        arg_type = Float64
        default = 1.0
    "--u-max"
        metavar = "U"
        help = "maximum U"
        arg_type = Float64
        default = 20.0
    "--u-step"
        metavar = "U"
        help = "U step"
        arg_type = Float64
    "--u-num"
        metavar = "N"
        help = "number of U"
        arg_type = Int
    "--u-log"
        help = "use logarithmic scale for U"
        action = :store_true
    "--t"
        metavar = "t"
        help = "t value"
        arg_type = Float64
        default = 1.0
end

add_arg_group(s, "entanglement entropy")
@add_arg_table s begin
    "--ee"
        metavar = "XA"
        help = "compute all EEs with partition size XA"
        arg_type = Int
        required = true
end
c = parsed_args = parse_args(ARGS, s, as_symbols=true)

# Number of sites
const M = c[:M]
# Number of particles
const N = c[:N]
# Output file
const output = c[:out]
# Site occupation restriction
const site_max = c[:site_max]
# Boundary conditions
const boundary = c[:boundary]
# Size of region A
const Asize = c[:ee]

if c[:u_log] && c[:u_num] === nothing
    println("--u-log must be used with --u-num")
    exit(1)
end

if c[:u_step] === nothing
    if c[:u_num] === nothing
        U_range = c[:u_min]:0.5:c[:u_max]
    else
        if c[:u_log]
            U_range = logspace(c[:u_min], c[:u_max], c[:u_num])
        else
            U_range = linspace(c[:u_min], c[:u_max], c[:u_num])
        end
    end
else
    if c[:u_num] === nothing
        U_range = c[:u_min]:c[:u_step]:c[:u_max]
    else
        println("--u-step and --u-num may not both be supplied")
        exit(1)
    end
end

if site_max === nothing
    const basis = Szbasis(M, N)
else
    const basis = RestrictedSzbasis(M, N, site_max)
end

#_______________________

ll=length(basis)
Vz=zeros(Float64, ll)
Vh=zeros(Float64, ll)
Vl=zeros(Float64, ll)
wf=zeros(Float64, ll)

for i=1:ll
   Vh[i]=0.1
   Vl[i]=0.1
   Vz[i]=1.0
end

if boundary==OBC
    num_links= basis.K-1
elseif boundary==PBC
    num_links= basis.K
end

for (i, bra) in enumerate(basis)
    cc=0
    for j=1: num_links
        j_next = j % basis.K + 1
        cc+=bra[j]*bra[j_next]
    end
    if cc== basis.N-1
        Vl[serial_num(basis, bra)]=1.0
    elseif cc==0
        Vh[serial_num(basis, bra)]=1.0
    end
end

Normh=0
Norml=0
Normz=0
for i=1:ll
   Normh+=Vh[i]^2
   Norml+=Vl[i]^2
   Normz+=Vz[i]^2
end

for i=1:ll
 Vh[i]/=sqrt(Normh)
 Vl[i]/=sqrt(Norml)
 Vz[i]/=sqrt(Normz)
end

#_______________________

open(output, "w") do f
    if site_max === nothing
        write(f, "# M=$(M), N=$(N), $(boundary)\n")
    else
        write(f, "# M=$(M), N=$(N), max=$(site_max), $(boundary)\n")
    end
    write(f, "# U/t E0/t S1(n=$(Asize)) S2(n=$(Asize)) S3(n=$(Asize))\n")
            wf=Vh
            wf=Vl
            wf=Vz

    for U in U_range

        # Create the Hamiltonian
        H = sparse_hamiltonian(basis, c[:t], U, boundary=boundary)
	print(" sparse_hamiltonian finish\n ")

        # Perform the Lanczos diagonalization to obtain the lowest eigenvector
        # http://docs.julialang.org/en/release-0.3/stdlib/linalg/?highlight=lanczos
        if U/c[:t]>1.5
            d = eigs(H, nev=1, which=:SR,tol=1e-12,v0=wf)
        elseif U/c[:t]<-1.5
            d = eigs(H, nev=1, which=:SR,tol=1e-12,v0=wf)
        else
            d = eigs(H, nev=1, which=:SR,tol=1e-12,v0=wf)
        end
        wf = vec(d[2][1:ll])
	warn("eigs finish",2)

        # Calculate the second Renyi entropy
        s3_particle = particle_entropy_mod(basis, Asize, wf, site_max)
        warn("finish finish finish finish finish")

        #s2_particle = particle_entropy(basis, Asize, wf)
        #s2_spatial, s2_operational = spatial_entropy(basis, Asize, wf)

        write(f, "$(U/c[:t]) $(d[1][1]/c[:t]) $(s3_particle[1]) $(s3_particle[2]) $(s3_particle[3])\n")
        flush(f)
    end
end
