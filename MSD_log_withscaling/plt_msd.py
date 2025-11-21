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
from matplotlib.ticker import FixedLocator, ScalarFormatter

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

h13 = np.loadtxt("NP-MSD")

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



#---- Define figure ----#
fig=plt.figure()
ax1 = fig.add_subplot(111)

#we prefer inside ticks for all plots
ax1.tick_params(axis='both',direction='in', which='both')

#---- Plotting first subplot -----#
# I have shown different type of linestyle that you can use but if you are showing the similar data
# keep the same line style something you are comparing then you can use two different linestyles 
ax1.errorbar(h13[:,0],h13[:,1],color=c3,lw=lscale*lwidth,linestyle='-',label='Nanoparticle')

#---- diffusion line ----#
x =  np.linspace(20000,1000000,num=1000)
y =  np.zeros(len(x))
y = y + (x**1)
scaley = 0.01*y
ax1.errorbar(x,scaley,color=c0, lw=lscale*lwidth, linestyle='--')
ax1.text(0.9,0.8,r'$t^{1}$', transform=ax1.transAxes,fontsize=10)

#---- Superdiffusion line ----#
x2 = np.linspace(0.001,0.7,num=1000)
y2 = np.zeros(len(x))
y2 = y2 + (x2**2)
scaley2 = 0.03*y2
ax1.errorbar(x2,scaley2,color=c0, lw=lscale*lwidth, linestyle=':')
ax1.text(0.07,0.27,r'$t^{2}$', transform=ax1.transAxes,fontsize=10)

#---- Subdiffusion line ----#
def GetFitRegion(arr1, arr2, a, b):
        SublogT = []; SublogMSD = []
        for i in range(len(arr1)):
                if arr1[i] > a and arr1[i] < b:
                        SublogT.append(math.log10(arr1[i]))
                        SublogMSD.append(math.log10(arr2[i]))
                else:
                        pass
        return SublogT, SublogMSD

def func1(x, a, b):
        return a*x + b

SublogT, SublogMSD  = GetFitRegion(h13[:,0], h13[:,1], 500, 5000)
Sub, Subcov = curve_fit(func1, SublogT, SublogMSD)
x=np.linspace(math.log10(500),math.log10(5000),num=1000)
y=np.zeros(len(x))
y=y+func1(x,*Sub)
x=np.power(10,x)
y=np.power(10,y)
sx32=x
sy32=y

ax1.plot(sx32,0.4*sy32, color="black", lw=lscale*lwidth, linestyle='-')
ax1.text(0.67,0.64,r'$t^{\alpha}$', transform=ax1.transAxes,fontsize=10)




#---- Set axis properties ----#

ax1.set_xlim([0.05,200000])
ax1.set_ylim([0.00001,6000])
ax1.set_yscale('log')
ax1.set_xscale('log')
ticks = [1e-4, 1e-3, 1e-2, 1e-1, 1, 1e1, 1e2, 1e3]

# Force these exact tick locations
ax1.yaxis.set_major_locator(FixedLocator(ticks))
#ax1.yaxis.set_minor_locator(FixedLocator([]))  # optional: no minor ticks

ax1.set_xlabel(r'$\Delta{t}$',labelpad=1)
ax1.set_ylabel(r'$\left<{{\Delta{r}}^2}\right>$',labelpad=1)

#---- Plot legend ----#
# Ensure legends are not overlapping with lines, you might want to adjust "loc" and "ncol"

legend=ax1.legend(loc="lower right",handlelength=2,numpoints=1,ncol=1,columnspacing=0.5,handletextpad=0.3,labelspacing=0.3) 
legend.get_frame().set_linewidth(-1.0)
legend.get_frame().set_alpha(0.0)

#---- Adjust the plots ----#
# Always ensure this part you might want to change the varible bottom
plt.subplots_adjust(left=0.17, bottom=0.17, right=0.99, top=0.99, wspace=0.0, hspace=0.0)

# ---- Save the files ----
# pdf is always the prefered file format to save plots
plt.savefig('Mean-square-displacement.png',transparent=True)
plt.savefig('Mean-square-displacement.pdf',transparent=True)

plt.show()
