#Plots the Von Neumann & Rényi Entanglement Entropies for equal particle bipartitions.
#System sizes plotted here: N = 2, 4, 6, 8, & 10 fermions

import numpy as np
import matplotlib.pyplot as plt

#Style file (Replace the next line with the directory where the desired stylefile is saved)
with plt.style.context('/Users/ecasiano/anaconda3/pkgs/matplotlib-1.5.3-np111py35_0/lib/python3.5/site-packages/matplotlib/style/IOP_large.mplstyle'):
    
    #Upload the data files (M=lattice size, N=particle number, n=particle partition size)
    
    #M=20, N=10, n=5
    datFileNEG_M20N10n5 = 'NA20F10n5NEGu.03_100l_ifP.dat'
    dataNEG_M20N10n5 = np.loadtxt(datFileNEG_M20N10n5)
    
    datFile_M20N10n5 = 'NA20F10n5u.03_100l_ifP.dat'
    data_M20N10n5 = np.loadtxt(datFile_M20N10n5)
    
    #M=16, N=8, n=4
    datFileNEG_M16N8n4 = 'NA16F8n4NEGu.03_100l_ifP.dat'
    dataNEG_M16N8n4 = np.loadtxt(datFileNEG_M16N8n4)
    
    datFile_M16N8n4 = 'NA16F8n4u.03_100l_ifP.dat'
    data_M16N8n4 = np.loadtxt(datFile_M16N8n4)
    
    #M=12, N=6, n=3
    datFileNEG_M12N6n3 = 'NA12F6n3NEGu.03_100l_ifP.dat'
    dataNEG_M12N6n3 = np.loadtxt(datFileNEG_M12N6n3)
    
    datFile_M12N6n3 = 'NA12F6n3u.03_100l_ifP.dat'
    data_M12N6n3 = np.loadtxt(datFile_M12N6n3)
    
    #M=8, N=4, n=2
    datFileNEG_M8N4n2 = 'NA8F4n2NEGu.03_100l_ifP.dat'
    dataNEG_M8N4n2 = np.loadtxt(datFileNEG_M8N4n2)
    
    datFile_M8N4n2 = 'NA8F4n2u.03_100l_ifP.dat'
    data_M8N4n2 = np.loadtxt(datFile_M8N4n2)
    
    #M=4, N=2, n=1
    datFileNEG_M4N2n1 = 'NA4F2n1NEGu.03_100l_ifP.dat'
    dataNEG_M4N2n1 = np.loadtxt(datFileNEG_M4N2n1)
    
    datFile_M4N2n1 = 'NA4F2n1u.03_100l_ifP.dat'
    data_M4N2n1 = np.loadtxt(datFile_M4N2n1)
    
    #Save the energies (U/t) variables
    energiesNEG = dataNEG_M16N8n4[:,0]
    energies = data_M16N8n4[:,0]
    
    energiesM4N2n1 = data_M4N2n1[:,0] #Note:There was data manually pasted to this case, and the energies have
    #different amount of elements than all other.
    
    #Save the Von Neumann (S1) & Renyi Entropies (S2) to variables
    
    #M=20, N=10, n=5
    s1NEG_M20N10n5 = dataNEG_M20N10n5[:,2]
    s1_M20N10n5 = data_M20N10n5[:,2]
    
    s2NEG_M20N10n5 = dataNEG_M20N10n5[:,3]
    s2_M20N10n5 = data_M20N10n5[:,3]
    
    #M=16, N=8, n=4
    s1NEG_M16N8n4 = dataNEG_M16N8n4[:,2]
    s1_M16N8n4 = data_M16N8n4[:,2]
    
    s2NEG_M16N8n4 = dataNEG_M16N8n4[:,3]
    s2_M16N8n4 = data_M16N8n4[:,3]
    
    #M=12, N=6, n=3
    s1NEG_M12N6n3 = dataNEG_M12N6n3[:,2]
    s1_M12N6n3 = data_M12N6n3[:,2]
    
    s2NEG_M12N6n3 = dataNEG_M12N6n3[:,3]
    s2_M12N6n3 = data_M12N6n3[:,3]
    
    #M=8, N=4, n=2
    s1NEG_M8N4n2 = dataNEG_M8N4n2[:,2]
    s1_M8N4n2 = data_M8N4n2[:,2]
    
    s2NEG_M8N4n2 = dataNEG_M8N4n2[:,3]
    s2_M8N4n2 = data_M8N4n2[:,3]
    
    #M=4, N=2, n=1
    s1NEG_M4N2n1 = dataNEG_M4N2n1[:,2]
    s1_M4N2n1 = data_M4N2n1[:,2]
    
    s2NEG_M4N2n1 = dataNEG_M4N2n1[:,3]
    s2_M4N2n1 = data_M4N2n1[:,3]
    
    #Note: When using symlog, set linthresx to at least 0.000001
    
    #Create figure
    fig = plt.figure()
    
    #Negative energies subplot
    ax1 = fig.add_subplot(121)
    ax1.axvline(x=-2,color='#cccccc')   #Grey vertical line at transition point
    ax1.plot(energiesNEG, s1NEG_M20N10n5, '-', label=r'$S1,N=10,n=5$', linewidth = 1, color='#5e4ea2')
    ax1.plot(energiesNEG, s1NEG_M16N8n4,  '-', label=r'$S1,N=8,n=4$',  linewidth = 1, color='#7dcba4')
    ax1.plot(energiesNEG, s1NEG_M12N6n3,  '-', label=r'$S1,N=6,n=3$',  linewidth = 1, color='#e95c47')
    ax1.plot(energiesNEG, s1NEG_M8N4n2,   '-', label=r'$S1,N=4,n=2$',  linewidth = 1, color='#4173b3')
    ax1.plot(energiesNEG, s1NEG_M4N2n1,   '-', label=r'$S1,N=2,n=1$',  linewidth = 1, color='#ff8c00')
    ax1.plot(energiesNEG, s2NEG_M20N10n5, ':', label=r'$S2,N=10,n=5$', linewidth = 2, color='#5e4ea2')
    ax1.plot(energiesNEG, s2NEG_M16N8n4,  ':', label=r'$S2,N=8,n=4$',  linewidth = 2, color='#7dcba4')
    ax1.plot(energiesNEG, s2NEG_M12N6n3,  ':', label=r'$S2,N=6,n=3$',  linewidth = 2, color='#e95c47')
    ax1.plot(energiesNEG, s2NEG_M8N4n2,   ':', label=r'$S2,N=4,n=2$',  linewidth = 2, color='#4173b3')
    ax1.plot(energiesNEG, s2NEG_M4N2n1,   ':', label=r'$S2,N=2,n=1$',  linewidth = 2, color='#ff8c00')
    ax1.set_xlim(-energies[-1], -energies[0])
    ax1.set_ylabel(r'$S_{\alpha}(n=\frac{N}{2}) - \ln{N \choose N/2}$')
    ax1.set_xscale('symlog', linthreshx = 0.000001)
    ax1.tick_params(axis='both', which='both', right='off', top='on',labelright='off')
    ax1.set_ylim(0,1.85)
    
    #Positive energies subplot
    ax2 = fig.add_subplot(122)
    ax2.axvline(x=2,color='#cccccc')   #Grey vertical line at transition point
    ax2.tick_params(axis='both', which='both', left='off', top='on',labelleft='off')
    ax2.plot(energies,       s1_M20N10n5, '-', label=r'$1, 10$', linewidth=1, color='#5e4ea2')
    ax2.plot(energies,       s1_M16N8n4,  '-', label=r'$1, 8$',  linewidth=1, color='#7dcba4')
    ax2.plot(energies,       s1_M12N6n3,  '-', label=r'$1, 6$',  linewidth=1, color='#e95c47')
    ax2.plot(energies,       s1_M8N4n2,   '-', label=r'$1, 4$',  linewidth=1, color='#4173b3')
    ax2.plot(energiesM4N2n1, s1_M4N2n1,   '-', label=r'$1, 2$',  linewidth=1, color='#ff8c00')
    ax2.plot(energies,       s2_M20N10n5, ':', label=r'$2, 10$', linewidth=2, color='#5e4ea2')
    ax2.plot(energies,       s2_M16N8n4,  ':', label=r'$2, 8$',  linewidth=2, color='#7dcba4')
    ax2.plot(energies,       s2_M12N6n3,  ':', label=r'$2, 6$',  linewidth=2, color='#e95c47')
    ax2.plot(energies,       s2_M8N4n2,   ':', label=r'$2, 4$',  linewidth=2, color='#4173b3')
    ax2.plot(energiesM4N2n1, s2_M4N2n1,   ':', label=r'$2, 2$',  linewidth=2, color='#ff8c00')
    ax2.set_xlim(energies[0], energies[-1])
    ax2.set_xscale('symlog', linthreshx = 0.000001)  #symlog necessary for log scale on negative values
    ax2.set_ylim(0,1.85)
    plt.xlabel(r'$V/t$',x=0)
    
    
    #Legend
    lgnd = plt.legend(loc=(0.03,0.075), fontsize=6, handlelength=3,handleheight=2,title=r'$\alpha$, $N$',frameon=False)
    lgnd.get_title().set_fontsize(6)
    lgnd.get_title().set_position((10.8,0))
    
    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)
    
    #Save the figure
    plt.savefig('entropiesVariousBipartitions.pdf')
    plt.savefig('entropiesVariousBipartitions.png')
    plt.show()

