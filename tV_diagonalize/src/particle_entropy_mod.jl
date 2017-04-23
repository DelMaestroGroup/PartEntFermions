"""
Calculate the particle entanglement entropy for a subset A, using the SVD on (A^*)A First test.
"""
function particle_entropy_mod(basis::AbstractSzbasis, Asize::Int, d::Vector{Float64}, MaxOccupation::Int)
    SRen = Array(Float64, 3)
    DimA=Int64
    DimB=Int64
    DimAdA=Int64
    for x = [:fN,:Wa,:Wb,:Flips,:SumFlips]
       @eval $x = Int64
    end
    norm= Float64
    facto= Float64
    L = basis.K
    N = basis.N
    Bsize = N - Asize
    if Asize>Bsize
        Asize,Bsize=Bsize,Asize 
    end
    # Dimensions of partition Hilbert spaces

    facto=1.0
    for i=1:Asize
	facto *=((1.0*L-i+1)/(1.0*i))
    end
    DimA = Int(round(facto))
    facto=1.0
    for i=1:Bsize
	facto *=((1.0*L-i+1)/(1.0*i))
    end
    DimB = Int(round(facto))

    DimAdA= min(DimA,DimB)
    const basisA = RestrictedSzbasis(L, Asize, MaxOccupation)
    const basisB = RestrictedSzbasis(L, Bsize, MaxOccupation)

    braA = Array(Int, L)
    braB = Array(Int, L)
    bra = Array(Int, L)
    # Matrix A
    Amatrix = zeros(Float64, DimA, DimB)
    # Weight factors
    Wa=factorial(Asize)
    Wb=factorial(Bsize)
    # Normalization coefficient
    norm=sqrt(Wa*Wb/factorial(basis.N))


    for (i, braA) in enumerate(basisA)
        for (j, braB) in enumerate(basisB)
	    bra=braA+braB
	    if bra in basis
		Flips=0
		SumFlips=0
		for k=1:L
		    Flips = Flips +(1-2* Flips)* braA[k]
		    SumFlips += Flips* braB[k]
		end
		Amatrix[i, j] = (-1)^ SumFlips*norm*d[serial_num(basis, bra)]
	    end
	end
    end

#    AdAmatrix = zeros(Float64, DimAdA, DimAdA)
#    for i=1:DimA
#        for j=1:DimA
#            for k=1:DimB
#               AdAmatrix[i,j]+= Amatrix[i,k]* Amatrix[j,k]
#	    end
#        end
#    end
    S = svdvals!(Amatrix)
    
    for i=1: DimAdA
        S[i]=S[i]^2
    end

    err = abs(sum(S) - 1.0)
    if err > 1e-12
        warn("RDM eigenvalue error ", err)
    end
    LogNn=log(factorial(basis.N)/factorial(Bsize)/factorial(Asize))
    SRen[1]=0
    for k=1:DimAdA
        if S[k]>0
            SRen[1] -=S[k]*log(S[k])
	end
    end
    SRen[1]=SRen[1]-LogNn
    SRen[2]=-log(sum(S.^2))-LogNn
    SRen[3]=-log(sum(S.^3))/2-LogNn
    warn(" AdA eigenvalue are", S)
    return SRen
end
