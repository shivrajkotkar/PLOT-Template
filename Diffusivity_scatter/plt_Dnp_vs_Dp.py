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

h10 = np.loadtxt("k_0")
h12 = np.loadtxt("k_5")
h13 = np.loadtxt("k_10")
h14 = np.loadtxt("k_20")
h15 = np.loadtxt("k_32")
h16 = np.loadtxt("k_70")

#---- Define colorscheme ----# 
  
n_curves = 9  
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
c6 = scalarMap.to_rgba(values[6])
c7 = scalarMap.to_rgba(values[7])
c8 = scalarMap.to_rgba(values[8])

# I usually define the number of datasets (e.g., +1 or +2 for the number of curves) and avoid using the last color in the colormap, as it’s often too light
# In this case, I have h10,h12 to h16 (6 datasets), so I did not use c1,and c7, and c8  
# lighter colors near the end of the colormap don’t print well in papers or presentations.
# You can skip one c values if colors are too close

#---- Define figure ----#
fig=plt.figure()
ax1 = fig.add_subplot(111)

ax1.tick_params(axis='both',direction='in', which='both')
#Here we are using two subplots stacked vertically. If you want a single plot instead, use ax1 = fig.add_subplot(111) and adjust the corresponding parameters

#---- Plotting first subplot -----#
# I prefer to use different markers (e.g., fmt='s') so that each curve can be visually distinguished.
ax1.errorbar(h10[:,3]*1000,h10[:,1]*1000,xerr=h10[:,4]*1000,yerr=h10[:,2]*1000,color=c0,lw=lscale*lwidth,fmt='o',label=r'$\kappa = 0$',markersize=msize)
ax1.errorbar(h12[:,3]*1000,h12[:,1]*1000,xerr=h12[:,4]*1000,yerr=h12[:,2]*1000,color=c2,lw=lscale*lwidth,fmt='<',label=r'$\kappa = 5$',markersize=msize)
ax1.errorbar(h13[:,3]*1000,h13[:,1]*1000,xerr=h13[:,4]*1000,yerr=h13[:,2]*1000,color=c3,lw=lscale*lwidth,fmt='v',label=r'$\kappa = 10$',markersize=msize)
ax1.errorbar(h14[:,3]*1000,h14[:,1]*1000,xerr=h14[:,4]*1000,yerr=h14[:,2]*1000,color=c4,lw=lscale*lwidth,fmt='s',label=r'$\kappa = 20$',markersize=msize)
ax1.errorbar(h15[:,3]*1000,h15[:,1]*1000,xerr=h15[:,4]*1000,yerr=h15[:,2]*1000,color=c5,lw=lscale*lwidth,fmt='^',label=r'$\kappa = 32$',markersize=msize)
ax1.errorbar(h16[:,3]*1000,h16[:,1]*1000,xerr=h16[:,4]*1000,yerr=h16[:,2]*1000,color=c6,lw=lscale*lwidth,fmt='D',label=r'$\kappa = 70$',markersize=msize)


#---- Set axis properties ----#

ax1.set_xlim([-0.1,3.1])
ax1.set_ylim([-0.5,10.5])
ax1.set_xticks([0,0.5,1.0,1.5,2.0,2.5,3.0])
ax1.set_yticks([0,2,4,6,8,10])
ax1.set_ylabel(r'$D_{\rm NP} \times 10^{3}$',labelpad=1)

ax1.set_xlabel(r'$D_{\rm P} \times 10^{3}$',labelpad=1)



#---- Plot legend ----#
# Ensure legends are not overlapping with lines, you might want to adjust "loc" and "ncol"

legend=ax1.legend(loc="lower right",handlelength=1,numpoints=1,ncol=2,columnspacing=0.5,handletextpad=0.3,labelspacing=0.3) 
legend.get_frame().set_linewidth(-1.0)
legend.get_frame().set_alpha(0.0)

#---- Adjust the plots ----#
# Always ensure this part you might want to change the varible bottom
plt.subplots_adjust(left=0.17, bottom=0.17, right=0.99, top=0.99, wspace=0.0, hspace=0.0)

# ---- Save the files ----
# pdf is always the prefered file format to save plots
plt.savefig('Dnp_vs_Dp.png',transparent=True)
plt.savefig('Dnp_vs_Dp.pdf',transparent=True)

plt.show()
