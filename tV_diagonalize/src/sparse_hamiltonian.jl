"""
Number of links for the boundary conditions.
"""
num_links(basis::AbstractSzbasis, boundary::BdryCond) = boundary == PBC ? basis.K : basis.K - 1

"""
Create a sparse Hamiltonian matrix for a PBC/OBC BH chain in 1D.

    H = -\\sum_{<i, j>} t_{i,j} (b_i^\\dagger b_j + b_i b_j^\\dagger) + (U/2) \\sum_i n_i (n_i - 1) - \\sum_i \\mu_i n_i
"""
function sparse_hamiltonian(basis::AbstractSzbasis, Ts::AbstractVector{Float64}, mus::AbstractVector{Float64}, U::Float64; boundary::BdryCond=PBC)
    end_site = num_links(basis, boundary)

    length(Ts) == end_site || error("Incorrect number of Ts: $(length(Ts)) != $(end_site)")
    length(mus) == basis.K || error("Incorrect number of mus: $(length(mus)) != $(basis.K)")

    rows = Int64[]
    cols = Int64[]
    elements = Float64[]

    for (i, bra) in enumerate(basis)
        # Diagonal part
        Usum = 0
        musum = 0
	#mus[1]=0.011
	#mus[2]=0.01
	#mus[3]=0.00001
	#mus[4]=0.00001
        for j=1:end_site
            musum += mus[j] * bra[j]
            j_next = j % basis.K + 1
            Usum += bra[j] * (bra[j_next])
        end

        push!(rows, i)
        push!(cols, i)
        push!(elements, U * Usum - musum)

        # Off-diagonal part
        for j=1:end_site
            j_next = j % basis.K + 1
            # Tunnel right, tunnel left.
            for (site1, site2) in [(j, j_next), (j_next, j)]
                if bra[site1] > 0
                    ket = copy(bra)
                    ket[site1] -= 1
                    ket[site2] += 1
                    if ket in basis
                        factor = 1
                        if j_next == 1
                            factor = (1)^(basis.N-1)
                        end
                        push!(rows, i)
                        push!(cols, serial_num(basis, ket))
                        push!(elements, -Ts[j] * sqrt(bra[site1]) * sqrt(bra[site2]+1) * factor)
                    end
                end
            end
        end
    end

    sparse(rows, cols, elements, length(basis), length(basis))
end

function sparse_hamiltonian(basis::AbstractSzbasis, Ts::AbstractVector{Float64}, U::Float64; boundary::BdryCond=PBC)
    sparse_hamiltonian(basis, Ts, zeros(basis.K), U, boundary=boundary)
end

function sparse_hamiltonian(basis::AbstractSzbasis, T::Float64, mus::AbstractVector{Float64}, U::Float64; boundary::BdryCond=PBC)
    sparse_hamiltonian(basis, fill(T, num_links(basis, boundary)), mus, U, boundary=boundary)
end

function sparse_hamiltonian(basis::AbstractSzbasis, T::Float64, U::Float64; boundary::BdryCond=PBC)
    sparse_hamiltonian(basis, fill(T, num_links(basis, boundary)), U, boundary=boundary)
end
