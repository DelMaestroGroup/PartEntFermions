#Plots the VonNeumann & Renyi Entanglement Entropies as functions of the energy U/t

import numpy as np
import matplotlib.pyplot as plt

#Replace directory in the next line with the one in which your desired stylefile resides
with plt.style.context('/Users/ecasiano/anaconda3/pkgs/matplotlib-1.5.3-np111py35_0/lib/python3.5/site-packages/matplotlib/style/IOP_large.mplstyle'):
    
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

    #Negative energies subplot
    ax1 = fig.add_subplot(121)
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
    lgnd = plt.legend(loc=(0.06,0.04),fontsize=7,handlelength=3,handleheight=2, title= r'$\alpha$, $N$')
    lgnd.get_title().set_fontsize(7)
    lgnd.get_title().set_position((12,0))
    
    #Positive energies subplot
    ax2 = fig.add_subplot(122)
    ax2.axvline(x=2, color='#cccccc')
    ax2.tick_params(axis='both', which='both', left='off', top='on',labelleft='off')
    ax2.plot(energies, s1_M28N14, '-',  label=r'$\alpha=1, N=14$', linewidth=1, color='#5e4ea2')
    ax2.plot(energies, s2_M28N14, '-',  label=r'$\alpha=2, N=14$', linewidth=1, color='#7dcba4')
    ax2.plot(energies, s1_M26N13, '--', label=r'$\alpha=1, N=13$', linewidth=2, color='#e95c47')
    ax2.plot(energies, s2_M26N13, '--', label=r'$\alpha=2, N=13$', linewidth=2, color='#4173b3')
    ax2.set_xlim(energies[0], energies[-1])
    ax2.set_xscale('symlog', linthreshx = 0.000001)
    plt.xlabel(r'$V/t$',x=0)
    
    #Inset Plot
    plt.subplots_adjust(wspace = 0.030)
    left,bottom,width,height = [0.3811,0.5,0.31,0.31]
    ax3 = fig.add_axes([left,bottom,width,height])
    ax3.plot(insetEnergies, s1_M28N14_3_3, '-',  label=r'$\alpha=1, N=14$',linewidth=1, color='#5e4ea2')
    ax3.plot(insetEnergies, s2_M28N14_3_3, '-',  label=r'$\alpha=2, N=14$',linewidth=1, color='#7dcba4')
    ax3.plot(insetEnergies, s1_M26N13_3_3, '--', label=r'$\alpha=1, N=13$',linewidth=2, color='#e95c47')
    ax3.plot(insetEnergies, s2_M26N13_3_3, '--', label=r'$\alpha=2, N=13$',linewidth=2, color='#4173b3')
    ax3.set_xlim(-2,2,1)
    ax3.set_ylim(0,0.4)
    ax3.xaxis.set_ticks([-2,-1,1,2])
    ax3.yaxis.set_ticks([0.0,0.1,0.2,0.3,0.4])


    #Save the figure
    plt.savefig('entropiesFigure.pdf', transparent=False)
    plt.savefig('entropiesFigure.png', transparent=False)
    plt.show()
