# mobius

from base import isPrime, mobius
import math
import matplotlib.pyplot as plt 
import numpy as np

def plotx(num):
    x = []
    
    for xcor in range(1,num+1):
        x.append(xcor)
        
    return x

def plotmoby(num):
    y = []

    for ycor in range(1,num+1):
        after = mobius(ycor)
        y.append(after)

    return y

plottingx = plotx(25)
plottingy = plotmoby(25)

plt.plot(plottingx, plottingy, marker = 'o', linestyle = '')
plt.xticks(np.arange(min(plottingx)-1, max(plottingx)+1, 1.0))
plt.yticks(np.arange(-1, 2, 1.0))
plt.xlabel("n")
plt.ylabel(u"\u03bc(n)")
plt.ylim([-1.5, 1.5])
plt.xticks()
plt.grid(True)
plt.show()
