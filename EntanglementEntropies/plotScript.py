#Top Plot: One Particle Entanglement entropy dependence on the interaction potential
#Bottom Plot: Entanglement entropies for equal particle number bipartitions at various system sizes

#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#This script technically generates two figures and combines them vertically into a single figure.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

with plt.style.context('../IOP_large.mplstyle2'):

#Top Plot: One Particle Entanglement entropy dependence on the interaction potential

    #Load data files

    datFileNEG_M28N14 = 'NA28F14n1NEGu.03_100l_ifP.dat'
    dataNEG_M28N14 = np.loadtxt(datFileNEG_M28N14)

    datFile_M28N14 = 'NA28F14n1u.03_100l_ifP.dat'
    data_M28N14 = np.loadtxt(datFile_M28N14)

    datFile_M28N14_3_3 = 'N1A28F14n1u_3_3.dat'
    data_M28N14_3_3 = np.loadtxt(datFile_M28N14_3_3)

    datFileNEG_M26N13 = 'NP26F13n1NEGu.03_100l_ifP.dat'
    dataNEG_M26N13 = np.loadtxt(datFileNEG_M26N13)

    datFile_M26N13 = 'NP26F13n1u.03_100l_ifP.dat'
    data_M26N13 = np.loadtxt(datFile_M26N13)

    datFile_M26N13_3_3 = 'N1P26F13n1u_3_3.dat'
    data_M26N13_3_3 = np.loadtxt(datFile_M26N13_3_3)

    #Load energies
    energiesNEG = dataNEG_M28N14[:,0]
    energies = data_M28N14[:,0]

    #Load energies for inset (inset data includes energy range U/t:[-3.0,3.0])
    insetEnergies = data_M28N14_3_3[:,0]

    #Save Entanglement Entropies (s1=VonNeumann, s2=Renyi) to variables
    #M=28, N=14
    s1NEG_M28N14 = dataNEG_M28N14[:,2]
    s1_M28N14 = data_M28N14[:,2]

    s2NEG_M28N14 = dataNEG_M28N14[:,3]
    s2_M28N14 = data_M28N14[:,3]

    #M=26, N=13
    s1NEG_M26N13 = dataNEG_M26N13[:,2]
    s1_M26N13 = data_M26N13[:,2]

    s2NEG_M26N13 = dataNEG_M26N13[:,3]
    s2_M26N13 = data_M26N13[:,3]

    #Saves entropies for the inset to variables
    s1_M28N14_3_3 = data_M28N14_3_3[:,2]
    s2_M28N14_3_3 = data_M28N14_3_3[:,3]

    s1_M26N13_3_3 = data_M26N13_3_3[:,2]
    s2_M26N13_3_3 = data_M26N13_3_3[:,3]


    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])


    #Negative energies subplot
    ax1 = plt.subplot(gs[0])
    #ax1 = fig.add_subplot(221)
    ax1.axvline(x=-2,color='#cccccc')   #Grey vertical line at transition point
    ax1.plot(energiesNEG, s1NEG_M28N14, '-',  label='1, 14', linewidth = 1, color='#5e4ea2')
    ax1.plot(energiesNEG, s2NEG_M28N14, '-',  label='2, 14', linewidth = 1, color='#7dcba4')
    ax1.plot(energiesNEG, s1NEG_M26N13, '--', label='1, 13', linewidth = 2, color='#e95c47')
    ax1.plot(energiesNEG, s2NEG_M26N13, '--', label='2, 13', linewidth = 2, color='#4173b3')
    ax1.set_xlim(-energies[-1], -energies[0])
    ax1.set_ylabel(r'$S_{\alpha}(n=1) - \ln({N})$')
    ax1.set_xscale('symlog', linthreshx = 0.000001)       #symlog necessary to plot negative values with log scale
    ax1.tick_params(axis='both', which='both', right='off', top='on',labelright='off')
    ax1.set_xlabel(' ')



    #Legend
    lgnd = plt.legend(loc=(0.06,0.04),fontsize=7,handlelength=3,handleheight=2, title= r'$\alpha$, $N$', frameon=False)
    lgnd = plt.legend(loc=(0.04,0.04),fontsize=7,handlelength=3,handleheight=2, title= r'$\alpha$, $N$', frameon=False)

    lgnd.get_title().set_fontsize(7)
    lgnd.get_title().set_position((12,0))

    #Positive energies subplot
    ax2 = plt.subplot(gs[1])
    #ax2 = fig.add_subplot(222)
    ax2.axvline(x=2, color='#cccccc')
    ax2.tick_params(axis='both', which='both', left='off', top='on',labelleft='off')
    ax2.plot(energies, s1_M28N14, '-',  label=r'$\alpha=1, N=14$', linewidth=1, color='#5e4ea2')
    ax2.plot(energies, s2_M28N14, '-',  label=r'$\alpha=2, N=14$', linewidth=1, color='#7dcba4')
    ax2.plot(energies, s1_M26N13, '--', label=r'$\alpha=1, N=13$', linewidth=2, color='#e95c47')
    ax2.plot(energies, s2_M26N13, '--', label=r'$\alpha=2, N=13$', linewidth=2, color='#4173b3')
    ax2.set_xlim(energies[0], energies[-1])
    ax2.set_xscale('symlog', linthreshx = 0.000001)
    #plt.xlabel(r'$V/t$',x=0)

    #Inset Plot
    plt.subplots_adjust(wspace = 0.030)

    left,bottom,width,height = [0.3811,0.60,0.31,0.31]
    ax3 = fig.add_axes([left,bottom,width,height])
    ax3.plot(insetEnergies, s1_M28N14_3_3, '-',  label=r'$\alpha=1, N=14$',linewidth=1, color='#5e4ea2')
    ax3.plot(insetEnergies, s2_M28N14_3_3, '-',  label=r'$\alpha=2, N=14$',linewidth=1, color='#7dcba4')
    ax3.plot(insetEnergies, s1_M26N13_3_3, '--', label=r'$\alpha=1, N=13$',linewidth=2, color='#e95c47')
    ax3.plot(insetEnergies, s2_M26N13_3_3, '--', label=r'$\alpha=2, N=13$',linewidth=2, color='#4173b3')
    ax3.set_xlim(-2,2,1)
    ax3.set_ylim(0,0.4)
    ax3.xaxis.set_ticks([-2,-1,1,2])
    ax3.yaxis.set_ticks([0.0,0.1,0.2,0.3,0.4])
    ax3.set_aspect(1.618033*4)

    
#Bottom Plot: Entanglement entropies for equal particle number bipartitions at various system sizes

#Load data 

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

    #Negative energies subplot
    ax4 = plt.subplot(gs[2], sharex=ax1)

    #ax4 = fig.add_subplot(223)
    ax4.axvline(x=-2,color='#cccccc')   #Grey vertical line at transition point
    ax4.plot(energiesNEG, s1NEG_M20N10n5, '-', label=r'$S1,N=10,n=5$', linewidth = 1, color='#5e4ea2')
    ax4.plot(energiesNEG, s1NEG_M16N8n4,  '-', label=r'$S1,N=8,n=4$',  linewidth = 1, color='#7dcba4')
    ax4.plot(energiesNEG, s1NEG_M12N6n3,  '-', label=r'$S1,N=6,n=3$',  linewidth = 1, color='#e95c47')
    ax4.plot(energiesNEG, s1NEG_M8N4n2,   '-', label=r'$S1,N=4,n=2$',  linewidth = 1, color='#4173b3')
    ax4.plot(energiesNEG, s1NEG_M4N2n1,   '-', label=r'$S1,N=2,n=1$',  linewidth = 1, color='#ff8c00')
    ax4.plot(energiesNEG, s2NEG_M20N10n5, ':', label=r'$S2,N=10,n=5$', linewidth = 2, color='#5e4ea2')
    ax4.plot(energiesNEG, s2NEG_M16N8n4,  ':', label=r'$S2,N=8,n=4$',  linewidth = 2, color='#7dcba4')
    ax4.plot(energiesNEG, s2NEG_M12N6n3,  ':', label=r'$S2,N=6,n=3$',  linewidth = 2, color='#e95c47')
    ax4.plot(energiesNEG, s2NEG_M8N4n2,   ':', label=r'$S2,N=4,n=2$',  linewidth = 2, color='#4173b3')
    ax4.plot(energiesNEG, s2NEG_M4N2n1,   ':', label=r'$S2,N=2,n=1$',  linewidth = 2, color='#ff8c00')
    ax4.set_xlim(-energies[-1], -energies[0])
    ax4.set_ylabel(r'$S_{\alpha}(n=\frac{N}{2}) - \ln{N \choose N/2}$')
    ax4.set_xscale('symlog', linthreshx = 0.000001)
    ax4.tick_params(axis='both', which='both', right='off', top='on',labelright='off')
    ax4.set_ylim(0,1.85)


    #Positive energies subplot
    ax5 = plt.subplot(gs[3], sharex=ax2)

    #ax5 = fig.add_subplot(224)
    ax5.axvline(x=2,color='#cccccc')   #Grey vertical line at transition point
    ax5.tick_params(axis='both', which='both', left='off', top='on',labelleft='off')
    ax5.plot(energies,       s1_M20N10n5, '-', label=r'$1, 10$', linewidth=1, color='#5e4ea2')
    ax5.plot(energies,       s1_M16N8n4,  '-', label=r'$1, 8$',  linewidth=1, color='#7dcba4')
    ax5.plot(energies,       s1_M12N6n3,  '-', label=r'$1, 6$',  linewidth=1, color='#e95c47')
    ax5.plot(energies,       s1_M8N4n2,   '-', label=r'$1, 4$',  linewidth=1, color='#4173b3')
    ax5.plot(energiesM4N2n1, s1_M4N2n1,   '-', label=r'$1, 2$',  linewidth=1, color='#ff8c00')
    ax5.plot(energies,       s2_M20N10n5, ':', label=r'$2, 10$', linewidth=2, color='#5e4ea2')
    ax5.plot(energies,       s2_M16N8n4,  ':', label=r'$2, 8$',  linewidth=2, color='#7dcba4')
    ax5.plot(energies,       s2_M12N6n3,  ':', label=r'$2, 6$',  linewidth=2, color='#e95c47')
    ax5.plot(energies,       s2_M8N4n2,   ':', label=r'$2, 4$',  linewidth=2, color='#4173b3')
    ax5.plot(energiesM4N2n1, s2_M4N2n1,   ':', label=r'$2, 2$',  linewidth=2, color='#ff8c00')
    ax5.set_xlim(energies[0], energies[-1])
    ax5.set_xscale('symlog', linthreshx = 0.000001)  #symlog necessary for log scale on negative values
    ax5.set_ylim(0,1.85)
    plt.xlabel(r'$V/t$',x=0)

    #Remove numbers from real axes of top plots
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.023)
    
    #Legend
    lgnd = plt.legend(loc=(0.03,0.075), fontsize=6, handlelength=3,handleheight=2,title=r'$\alpha$, $N$',frameon=False)
    lgnd.get_title().set_fontsize(6)
    lgnd.get_title().set_position((10.8,0))

    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)

    plt.savefig('entanglementEntropies.pdf', transparent=False)
    plt.savefig('entanglementEntropies.png', transparent=False)
    plt.show()