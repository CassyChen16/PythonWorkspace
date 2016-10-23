'''
@Author: Cassy Chen
@Date: Oct. 23, 2016
@Description: Pyplot tutorial examples
'''

import numpy as np
from matplotlib import pyplot as plt 

# Plotting a figure with specific y-axis and default x-axis
def defaultPlotX():
    plt.plot([1, 2, 3, 4]) # Default x-axis has the sample length with y-axis, but starts with 0
    plt.ylabel('some numbers')
    plt.show()

# defaultPlotY() # for test purpose

def plotXY():
    plt.plot([1,2,3,4], [1,4,9,16], 'ro') # Plot(x, y, line style=red circle) 
    plt.axis([0, 6, 0, 20]) # x-axis range is [0,6], y-axis range is [0,20]
    plt.show() # axis range is given, shown in axis

# plotXY()

def plotMutiLines():
    # evenly sampled [0., 5.] at 0.2 invervals
    t = np.arange(0., 5., 0.2) 

    # Plot red dashes, blue squares, and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    # axis is not given, axis is decided by plot range
    plt.show()

# plotMutiLines()

def plotTwoSubplots():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    ft1 = np.exp(-t1) * np.cos(2*np.pi*t1)
    ft2 = np.exp(-t2) * np.cos(2*np.pi*t2)
    
    plt.figure(1)
    # subplot command specifies numrows, numcols, fignums
    # fignums in [1, numrows*numcols]
    # if numrows*numcols < 10, subplot(211) is identical to subplot(2,1,1)
    plt.subplot(211) 
    plt.plot(t1, ft1, 'bo', t2, ft2, 'k')

    plt.figure(2)
    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

    plt.show()

# plotTwoSubplots()




