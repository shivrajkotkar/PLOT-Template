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
fig_height = 2*fig_width/1.5 # height in inches
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

h10 = np.loadtxt("c_0.025")
h11 = np.loadtxt("c_0.05")
h12 = np.loadtxt("c_0.075")
h13 = np.loadtxt("c_0.1")
h14 = np.loadtxt("c_0.15")
h15 = np.loadtxt("c_0.2")
h16 = np.loadtxt("c_0.3")
h17 = np.loadtxt("c_0.4")

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
# In this case, I have h10 to h17 (8 datasets), so I did not use c8  
# lighter colors near the end of the colormap don’t print well in papers or presentations.


#---- Define figure ----#
fig=plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.tick_params(axis='both',direction='in', which='both')
ax2.tick_params(axis='both',direction='in', which='both')
#Here we are using two subplots stacked vertically. If you want a single plot instead, use ax1 = fig.add_subplot(111) and adjust the corresponding parameters

#---- Plotting first subplot -----#
# I prefer to use different markers (e.g., fmt='s') so that each curve can be visually distinguished.
ax1.errorbar(h10[:,0],h10[:,1]*1000,xerr=None,yerr=h10[:,2]*1000,color=c0,lw=lscale*lwidth,linestyle='-',fmt='o',fillstyle='full',label=r'$c=0.025$',markersize=msize)
ax1.errorbar(h11[:,0],h11[:,1]*1000,xerr=None,yerr=h11[:,2]*1000,color=c1,lw=lscale*lwidth,linestyle='-',fmt='>',fillstyle='full',label=r'$c=0.05$',markersize=msize)
ax1.errorbar(h12[:,0],h12[:,1]*1000,xerr=None,yerr=h12[:,2]*1000,color=c2,lw=lscale*lwidth,linestyle='-',fmt='<',fillstyle='full',label=r'$c=0.075$',markersize=msize)
ax1.errorbar(h13[:,0],h13[:,1]*1000,xerr=None,yerr=h13[:,2]*1000,color=c3,lw=lscale*lwidth,linestyle='-',fmt='v',fillstyle='full',label=r'$c=0.1$',markersize=msize)
ax1.errorbar(h14[:,0],h14[:,1]*1000,xerr=None,yerr=h14[:,2]*1000,color=c4,lw=lscale*lwidth,linestyle='-',fmt='s',fillstyle='full',label=r'$c=0.15$',markersize=msize)
ax1.errorbar(h15[:,0],h15[:,1]*1000,xerr=None,yerr=h15[:,2]*1000,color=c5,lw=lscale*lwidth,linestyle='-',fmt='^',fillstyle='full',label=r'$c=0.2$',markersize=msize)
ax1.errorbar(h16[:,0],h16[:,1]*1000,xerr=None,yerr=h16[:,2]*1000,color=c6,lw=lscale*lwidth,linestyle='-',fmt='D',fillstyle='full',label=r'$c=0.3$',markersize=msize)
ax1.errorbar(h17[:,0],h17[:,1]*1000,xerr=None,yerr=h17[:,2]*1000,color=c7,lw=lscale*lwidth,linestyle='-',fmt='h',fillstyle='full',label=r'$c=0.4$',markersize=msize)

#---- Plotting second subplot -----#
ax2.errorbar(h10[:,0],h10[:,3]*1000,xerr=None,yerr=h10[:,4]*1000,color=c0,lw=lscale*lwidth,linestyle='--',fmt='o',fillstyle='none',label=r'$c=0.025$',markersize=msize)
ax2.errorbar(h11[:,0],h11[:,3]*1000,xerr=None,yerr=h11[:,4]*1000,color=c1,lw=lscale*lwidth,linestyle='--',fmt='>',fillstyle='none',label=r'$c=0.05$',markersize=msize)
ax2.errorbar(h12[:,0],h12[:,3]*1000,xerr=None,yerr=h12[:,4]*1000,color=c2,lw=lscale*lwidth,linestyle='--',fmt='<',fillstyle='none',label=r'$c=0.075$',markersize=msize)
ax2.errorbar(h13[:,0],h13[:,3]*1000,xerr=None,yerr=h13[:,4]*1000,color=c3,lw=lscale*lwidth,linestyle='--',fmt='v',fillstyle='none',label=r'$c=0.1$',markersize=msize)
ax2.errorbar(h14[:,0],h14[:,3]*1000,xerr=None,yerr=h14[:,4]*1000,color=c4,lw=lscale*lwidth,linestyle='--',fmt='s',fillstyle='none',label=r'$c=0.15$',markersize=msize)
ax2.errorbar(h15[:,0],h15[:,3]*1000,xerr=None,yerr=h15[:,4]*1000,color=c5,lw=lscale*lwidth,linestyle='--',fmt='^',fillstyle='none',label=r'$c=0.2$',markersize=msize)
ax2.errorbar(h16[:,0],h16[:,3]*1000,xerr=None,yerr=h16[:,4]*1000,color=c6,lw=lscale*lwidth,linestyle='--',fmt='D',fillstyle='none',label=r'$c=0.3$',markersize=msize)
ax2.errorbar(h17[:,0],h17[:,3]*1000,xerr=None,yerr=h17[:,4]*1000,color=c7,lw=lscale*lwidth,linestyle='--',fmt='h',fillstyle='none',label=r'$c=0.4$',markersize=msize)

#---- Set axis properties ----#

#---- Nanoparticle ----#
ax1.set_xlim([-3,73])
ax1.set_ylim([0.13,13])
ax1.set_xticks([0,10,20,30,40,50,60,70])
ax1.set_yscale('log')
ax1.set_ylabel(r'$D_{\rm NP} \times 10^{3}$',labelpad=6)
ax1.text(0.9,0.9,"(a)", transform=ax1.transAxes)
plt.setp(ax1.get_xticklabels(), visible=False)  # Draws ticks only (no labels) when axes share an axis.

#---- Polymer COM ----#
ax2.set_xlim([-3,73])
ax2.set_ylim([0.04,4.0])
ax2.set_yscale('log')
ax2.set_xticks([0,10,20,30,40,50,60,70])
ax2.set_ylabel(r'$D_{\rm P} \times 10^{3}$',labelpad=0)
ax2.text(0.9,0.9,"(b)", transform=ax2.transAxes)

plt.xlabel(r'$\kappa$',labelpad=1)


#---- Plot legend ----#
# Plot legend — only one set of legends is shown here (for ax1). 
# You can also display a legend for ax2, but it’s omitted here due to lack of space in plotting area.

legend=ax1.legend(loc="lower right",handlelength=1,numpoints=1,ncol=2,columnspacing=0.5,handletextpad=0.3,labelspacing=0.3) 
legend.get_frame().set_linewidth(-1.0)
legend.get_frame().set_alpha(0.0)

#---- Adjust the plots ----#
# Always ensure this part you might want to change the varible bottom
plt.subplots_adjust(left=0.17, bottom=0.09, right=0.99, top=0.99, wspace=0.0, hspace=0.0)

# ---- Save the files ----
# pdf is always the prefered file format to save plots
plt.savefig('D-all-log.png',transparent=True)
plt.savefig('D-all-log.pdf',transparent=True)

plt.show()
