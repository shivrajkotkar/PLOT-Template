import matplotlib.pyplot as plt
import numpy as np

#!/usr/bin/env python
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import math
import matplotlib.colors as colors
import matplotlib.cm as cmx
#import colormaps as cmaps
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline
from matplotlib import rcParams
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.font_manager as fm

n_curves = 8
values = range(n_curves)
jet = cm = plt.get_cmap('magma')
cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
cdata = scalarMap.to_rgba(values)

c0 = scalarMap.to_rgba(values[0])
c1 = scalarMap.to_rgba(values[1])
c2 = scalarMap.to_rgba(values[2])
c3 = scalarMap.to_rgba(values[3])
c4 = scalarMap.to_rgba(values[4])
c5 = scalarMap.to_rgba(values[5])
c6 = scalarMap.to_rgba(values[6])
c7 = scalarMap.to_rgba(values[7])
arial_path= "arial.ttf"
arial_font= fm.FontProperties(fname=arial_path, size=30)


legend_font = fm.FontProperties(fname=arial_path, size=20)  # Adjust size as needed


sets = np.array([
    [-6.35917, -7.09918, -6.5451, -5.45, -5.67962, -6.25333, -9.10702],
[-6.84, -7.45556, -6.7108, -6.85964, -6.16429, -8.65724, -8.38613],
[-6.2125, -7.07918, -6.4412, -6.345, -7.52429, -8.19707, -9.22844],
[-4.43429, -5.93556, -5.7286, -4.78714, -4.99667, -5.44667, -8.79083]
])

set_errors = np.array([
     [0.335192, 0.18957, 0.0147369, 0.369414, 0.16612, 0.177501, 0.145],
 [0.293121, 0.320518, 0.0641058, 0.446828, 0.528579, 0.388172, 0.886],
 [0.553708, 0.204398, 0.00328261, 0.572756, 0.432391, 0.260521, 0.614],
 [0.269744, 0.157342, 0.0035051, 0.190582, 0.213854, 0.181751, 0.1760]
])

sets_divided = sets / 0.5922
set_errors_divided = set_errors / 0.5922

array1_transposed = sets_divided.T
errors1_transposed = set_errors_divided.T

set1, set2, set3, set4, set5, set6, set7 = array1_transposed
set1_errors_1, set2_errors_1, set3_errors_1, set4_errors_1, set5_errors_1, set6_errors_1, set7_errors_1 = errors1_transposed


sets2=  np.array([
[-7.04333, -7.21826, -6.525 ,-7.1375, -8.04222 ,-8.5375, -6.698],
[-4.1055, -5.86826, -5.6644 ,-4.07412, -4.84932, -5.0875, -7.00],
[-6.98028, -6.20673, -5.61 , -6.29583 ,-6.61333, -6.83, -6.573],
[-5.83875, -7.0725, -6.35271, -5.536  ,-6.27, -6.16429, -9.03882]
])

set2_errors= np.array([  [0.410406, 0.273783 ,0.0212132, 0.383351 ,0.246423, 0.343182, 0.549488],
 [0.333742, 0.16228 ,0.0240034 ,0.261607 ,0.112733, 0.125328, 0.05],
 [0.547496 ,0.296039,0.05,  0.389637 ,0.237157 ,0.178191, 0.266093],
 [0.339724 ,0.515, 0.00706793, 0.2869,0.362,  0.204966, 0.489871]])


sets2_divided = sets2 / 0.5922
set2_errors_divided = set2_errors / 0.5922

array2_transposed = sets2_divided.T
errors2_transposed = set2_errors_divided.T

set1_2, set2_2, set3_2, set4_2, set5_2, set6_2, set7_2 = array2_transposed
set1_errors_2, set2_errors_2, set3_errors_2, set4_errors_2, set5_errors_2, set6_errors_2, set7_errors_2 = errors2_transposed


sets3= np.array([[-4.94231,-5.02375,
-4.91484,
-4.73786,
-4.79541,
-5.00053, -6.255],
[-3.86714,
-5.64905,
-5.813,
-4.52759,
-5.13057,
-5.30125, -4.88],
[-4.194,
-5.22387,
-4.9086,
-4.62435,
-5.03839,
-5.68, -5.66381],
[-5.433,
-5.13353,
-5.3794,
-4.54667,
-5.06042,
-5.44733, -5.043]])

set3_errors =np.array([
[0.360327,
0.274795,
0.0117958,
0.183027,
0.0915786,
0.0345565, 0.3448
],
 [0.351428,
0.321262,
0.00543984,
0.219393,
0.131752,
0.06854, 0.311127],
 
 [0.37186,
0.116467,
0.0035051,
0.244314,
0.114894,
0.188892, 0.3671],

 [0.45063,
0.24736,
0.0248596,
0.34089,
0.138225,
0.242295, 0.280568]])

sets3_divided =sets3/0.5922
set3_errors_divided = set3_errors/0.5922

array3_transposed = sets3_divided.T
errors3_transposed = set3_errors_divided.T

set1_3, set2_3, set3_3, set4_3, set5_3, set6_3, set7_3 = array3_transposed
set1_errors_3, set2_errors_3, set3_errors_3, set4_errors_3, set5_errors_3, set6_errors_3, set7_errors_3 = errors3_transposed


x_labels_1 = ['bc', f'bc${chr(773)}$', f'b${chr(773)}$c', f'b${chr(773)}$c${chr(773)}$']
x_labels_2 = ['ac', f'ac${chr(773)}$', f'a${chr(773)}$c', f'a${chr(773)}$c${chr(773)}$']
x_labels_3 = ['ab', f'ab${chr(773)}$', f'a${chr(773)}$b', f'a${chr(773)}$b${chr(773)}$']



x1 = np.arange(len(sets))
x2=np.arange(len(sets))
x3=np.arange(len(sets))
# Create subplots

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6), constrained_layout=True)
width = 0.12

# Iterate over subplots
for i, ax in enumerate(axes):
    # Select the dataset & x-values for each subplot
    if i == 0:
        x, data_sets, data_errors, x_labels = x1, [set4, set6, set1, set5, set2, set3, set7], [set4_errors_1, set6_errors_1, set1_errors_1, set5_errors_1, set2_errors_1, set3_errors_1, set7_errors_1], x_labels_1
    elif i == 1:
        x, data_sets, data_errors, x_labels = x2, [set4_2, set6_2, set1_2, set5_2, set2_2, set3_2, set7_2], [set4_errors_2, set6_errors_2, set1_errors_2, set5_errors_2, set2_errors_2, set3_errors_2, set7_errors_2], x_labels_2
    else:
        x, data_sets, data_errors, x_labels = x3, [set4_3, set6_3, set1_3, set5_3, set2_3, set3_3, set7_3], [set4_errors_3, set6_errors_3, set1_errors_3, set5_errors_3, set2_errors_3, set3_errors_3, set7_errors_3], x_labels_3 

    # Plot bars for the current subplot
    ax.bar(x - 3*width, data_sets[0], width, yerr=data_errors[0], capsize=5, color=c1, label='CQ', edgecolor='black', linewidth=1.2)
    ax.bar(x - 2*width, data_sets[1], width, yerr=data_errors[1], capsize=5, color=c2, label='QN', edgecolor='black', linewidth=1.2)
    ax.bar(x - width, data_sets[2], width, yerr=data_errors[2], capsize=5, color=c3, label='AQ', edgecolor='black', linewidth=1.2)
    ax.bar(x, data_sets[3], width, yerr=data_errors[3], capsize=5, color=c4, label='MQ', edgecolor='black', linewidth=1.2)
    ax.bar(x + width, data_sets[4], width, yerr=data_errors[4], capsize=5, color=c5, label='ARS', edgecolor='black', linewidth=1.2)
    ax.bar(x + 2*width, data_sets[5], width, yerr=data_errors[5], capsize=5, color=c6, label='ART', edgecolor='black', linewidth=1.2)
    ax.bar(x + 3*width, data_sets[6], width, yerr=data_errors[6], capsize=5, color='tab:grey', label='Heme', edgecolor='black', linewidth=1.2)

    # Set thick borders
    for spine in ['top', 'bottom', 'left', 'right']:
        ax.spines[spine].set_linewidth(3)

    # Set x-axis labels (Different for each subplot)
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels,fontproperties=arial_font)
    ax.tick_params(axis='x', pad =6)
    # Set y-axis ticks & labels
    ax.set_yticks(np.arange(-18, 0, 4))
    ax.set_ylim(-18, 0)

    # Remove y-axis labels for Subplot 2 & 3
    if i == 0:
        ax.set_ylabel(r'$\Delta$G (kT)', fontproperties=arial_font)
        ax.set_yticklabels(ax.get_yticks(), fontproperties=arial_font)  # Set font size for y-tick labels
    else:
        ax.set_yticklabels([])  # Hide y labels for subplot 2 & 3

    # Tick styling
    ax.tick_params(direction='in', axis='both', width=3, length=8)
    if i==2:
        ax.legend(loc='lower center', ncol=4, frameon=False, markerscale=3, prop=legend_font, handletextpad=0.25, columnspacing=0.3, bbox_to_anchor=(0.53, 0.15))

# Adjust layout for spacing between subplots
#ax.subplots_adjust(wspace=2.5)  # This adjusts the space between subplots

# Save and show
plt.savefig('Kink_all.png')
plt.show()
