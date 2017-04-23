"""
Calculate the particle entanglement entropy for a subset A, using the SVD.
"""
function particle_entropy(basis::AbstractSzbasis, Asize::Int, d::Vector{Float64})
    SRen = Array(Float64, 4)
    #rows = Int64[]
    #cols = Int64[]
    #elements = Float64[]
    M = basis.K
    Bsize = basis.N - Asize
    # Dimensions of partition Hilbert spaces
    DimA = M^Asize
    DimB = M^Bsize

    # Matrix to SVD
    Amatrix = zeros(Float64, DimA, DimB)

    fN = factorial(basis.N)
    occupA = Array(Int, M)
    occup = Array(Int, M)
     vcount=0
    for i=1:DimA
        fill!(occupA, 0)

        Sone = 1
        for k=1:Asize
 
            c = 0
            for s = 1: div(i - 1, M^(k - 1)) % M   #Modification starts
                c += occupA[s]
            end
            Sone = Sone * (-1)^c

            occupA[1 + div(i - 1, M^(k - 1)) % M] += 1
        end

        for j=1:DimB
            copy!(occup, occupA)
            
            Stwo = 1
            for k=1:Bsize

                c = 0
                for s = 1: div(j - 1, M^(k - 1)) % M   #Modification starts
                    c += occup[s]
                end
                Stwo = Stwo * (-1)^c

 
                occup[1 + div(j - 1, M^(k - 1)) % M] += 1
            end

            if occup in basis
                norm = 1 / fN
		vcount+=1
                #for x in occup
                #    norm *= factorial(x)
                #end

                Amatrix[i, j] = (Sone * Stwo)^1 *  sqrt(norm) * d[serial_num(basis, occup)]
	        #push!(rows, i)
       		#push!(cols, j)
        	#push!(elements, (Sone * Stwo)^1 *  sqrt(norm) * d[serial_num(basis, occup)])

            end
        end
warn("push ",i,"vcount ", vcount)
    end
    #Asparse=sparse(rows, cols, elements, DimA,  DimB)
    SS = svdvals!(Amatrix)
warn("svds start",4)
    #SS = svds(sparse(rows, cols, elements, DimA,  DimB),nsv= min(DimA,DimB),ritzvec=false)[1][:S]
    
    err = abs(sum(SS.^2) - 1.0)
    if err > 1e-12
        warn("RDM eigenvalue error ", err)
    end
    LogNn=log(factorial(basis.N)/factorial(Bsize)/factorial(Asize))
    SRen[1]=0
    for k=1:min(DimA,DimB)
    SRen[1] -=SS[k]^2*log(SS[k]^2)
    end
    SRen[1]=SRen[1]-LogNn
    SRen[2]=-log(sum(SS.^4))-LogNn
    SRen[3]=-log(sum(SS.^6))/2-LogNn
    return SRen
end
