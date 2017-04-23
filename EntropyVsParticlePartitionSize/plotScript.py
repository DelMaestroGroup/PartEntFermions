#Plots the VonNeumann & Rényi Entanglement Entropies as functions of log(N choose n)
#where N is the number of fermions in the 1D lattice and n is the size of the particle partition.
#An inset is included in which the VonNeumann entropy is studied as a function of the particle partition n.

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom 

#Principal Plot

#Replace the directory in the following line with the one in which your desired stylefile resides
with plt.style.context('IOP_large.mplstyle'):


    #Load the data file
    datFile = 'NA20F10n1_n5.dat'
    data = np.loadtxt(datFile)

    #Load partition sizes (n)
    partitionSizes = data[:,0]

    #Calculate the binomial coefficient (N choose n)
    N = 10                                           #Number of particles
    N_choose_n = binom(N,partitionSizes)


    #Save the entanglement entropies (s1=VonNeumman , s2=Rényi)
    #For M=20, N=10, n=1
    s1 = data[:,3]
    s2 = data[:,4]

    #Plot
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(np.log(N_choose_n), s1 + np.log(N_choose_n), 'o-', label=r'$\alpha=1$', linewidth = 1.0, color='#5e4ea2',    mec='#5e4ea2', mfc='None', ms=5, mew=1.0)
    ax1.plot(np.log(N_choose_n), s2 + np.log(N_choose_n), 's-', label=r'$\alpha=2$', linewidth = 1.0, color='#7dcba4', mec='#7dcba4', mfc='None', ms=5, mew=1.0)
    ax1.set_xlim(2.2,5.7)
    ax1.set_ylim(2.2,6.0)
    ax1.set_ylabel(r'$S_{\alpha}(n)$')
    ax1.set_xlabel(r'$\ln{{N}\choose{n}}$')
    ax1.legend(loc='upper left', numpoints=1)
  
    #Note: In lines 32 & 33, log(N_choose_n) is being added to the entropy. The code subtracts this term from the entropy
    #but the entropy (withou the subtraction of the binomial coefficient) is the value of interest in this plot
    
    #Add text with parameters used
    ax1.text(2.35,4.65, r'$V/t=1, N=10$', fontsize=11)

#Inset Plot

with plt.style.context('/Users/ecasiano/anaconda3/pkgs/matplotlib-1.5.3-np111py35_0/lib/python3.5/site-packages/matplotlib/style/IOP_small.mplstyle'):

    #Location of the inset
    left, bottom, width, height = [0.62, 0.25, 0.24, 0.24]
    ax2 = fig.add_axes([left,bottom,width,height])
    
    ax2.plot(partitionSizes, s1, color='#5e4ea2', marker='o', mec='#5e4ea2', mfc='None', ms=3, mew=0.8)
    ax2.set_xlabel(r'$n$', labelpad=0.1)
    ax2.set_yticks([0.06,0.10,0.14,0.18,0.22])
    ax2.set_xticks([1,2,3,4,5])
    ax2.set_xlim(0.85,5.15)

    #Save and show
    plt.savefig('SvsN_choose_N.pdf')
    plt.savefig('SvsN_choose_N.png')
    plt.show()
