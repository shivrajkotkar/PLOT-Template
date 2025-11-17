#!/usr/bin/env python

#---- import necessary packages ----#

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.colors as colors
import matplotlib.cm as cmx
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline
from matplotlib import rcParams
from matplotlib.legend_handler import HandlerLine2D

#---- define parameters for plotting like figure size, linesize, and markersize ----#
fig_width = 3.25 # width in inches
fig_height = fig_width/1.33 # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'Agg',
          'axes.labelsize': 9,
          'axes.titlesize': 9,
          'font.size': 9,
          'xtick.labelsize': 9,
          'ytick.labelsize': 9,
          'figure.figsize': fig_size,
          'savefig.dpi' : 600,
          'font.family': 'sans-serif',
          'axes.linewidth' : 1.0,
          'xtick.major.size' : 5,
          'ytick.major.size' : 5,
          'xtick.top': 'False',
          'xtick.bottom': 'True',
          'ytick.left': 'True',
          'ytick.right': 'True',
          'svg.fonttype' : 'none',
          'pdf.fonttype' : 42
          }

rcParams.update(params)
lwidth= 0.8
lscale = 1.5
msize = 6

#---- Load the Data ----# 

# It’s a good practice to save processed data in text files and use them for plotting
# I’ve often seen people perform complex calculations within plotting scripts. If possible, avoid this except when performing fitting analysis

h11 = np.loadtxt("gamma_4.4")
h12 = np.loadtxt("gamma_10")
h13 = np.loadtxt("gamma_25")
h14 = np.loadtxt("gamma_50")

#---- Define colorscheme ----# 
  
n_curves = 6  
values = range(n_curves)
cmap = plt.get_cmap('magma')  #You can also try 'viridis', 'plasma'  
cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cmap)

# Here we define n_curve variables

c0 = scalarMap.to_rgba(values[0])
c1 = scalarMap.to_rgba(values[1])
c2 = scalarMap.to_rgba(values[2])
c3 = scalarMap.to_rgba(values[3])
c4 = scalarMap.to_rgba(values[4])
c5 = scalarMap.to_rgba(values[5])

# I usually define the number of datasets (e.g., +1 or +2 for the number of curves) and avoid using the last color in the colormap, as it’s often too light
# In this case, I have h11 to h14 (4 datasets), so I did not use c0 and c5  
# lighter colors near the end of the colormap don’t print well in papers or presentations.


#---- Define figure ----#
fig=plt.figure()
ax1 = fig.add_subplot(111)

#we prefer inside ticks for all plots
ax1.tick_params(axis='both',direction='in', which='both')

#---- Plotting first subplot -----#
# I have shown different type of linestyle that you can use but if you are showing the similar data
# keep the same line style something you are comparing then you can use two different linestyles 
ax1.errorbar(h11[:,0],h11[:,1],color=c1,lw=lscale*lwidth,linestyle='-',label=r'$\gamma = 4.4$')
ax1.errorbar(h12[:,0],h12[:,1],color=c2,lw=lscale*lwidth,linestyle=':',label=r'$\gamma = 10$')
ax1.errorbar(h13[:,0],h13[:,1],color=c3,lw=lscale*lwidth,linestyle='--',label=r'$\gamma = 25$')
ax1.errorbar(h14[:,0],h14[:,1],color=c4,lw=lscale*lwidth,linestyle='-.',label=r'$\gamma = 50$')


#---- Set axis properties ----#

ax1.set_xlim([-1,61])
ax1.set_ylim([0.00005,5])
ax1.set_xticks([0,10,20,30,40,50,60])
ax1.set_yticks([0.0001,0.001,0.01,0.1,1])

ax1.set_yscale('log')
ax1.set_ylabel(r'$\rho (r)$',labelpad=1)
ax1.set_xlabel(r'$r$',labelpad=1)



#---- Plot legend ----#
# Ensure legends are not overlapping with lines, you might want to adjust "loc" and "ncol"

legend=ax1.legend(loc="upper right",handlelength=2,numpoints=1,ncol=1,columnspacing=0.5,handletextpad=0.3,labelspacing=0.3) 
legend.get_frame().set_linewidth(-1.0)
legend.get_frame().set_alpha(0.0)

#---- Adjust the plots ----#
# Always ensure this part you might want to change the varible bottom
plt.subplots_adjust(left=0.17, bottom=0.17, right=0.99, top=0.99, wspace=0.0, hspace=0.0)

# ---- Save the files ----
# pdf is always the prefered file format to save plots
plt.savefig('Monomer_density.png',transparent=True)
plt.savefig('Monomer_density.pdf',transparent=True)

plt.show()
