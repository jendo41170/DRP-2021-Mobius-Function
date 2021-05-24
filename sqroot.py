# square root

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
    numsum = 0

    for ycor in range(1,num+1):
        after = mobius(ycor)
        numsum += after
        y.append(numsum)

    return y

xlist=plotx(5000)
ylist=plotmoby(5000)
x = np.linspace(1, 5000, 5000)
y = np.sqrt(x)
y2 = (-1) * np.sqrt(x)

plt.plot(xlist, ylist, label = 'M(n)')
plt.plot(x,y,label = '\u221An')
plt.plot(x,y2, label = '-\u221An')
plt.xlabel('n')
#plt.xticks(np.arange(min(xlist)-1, max(xlist)+1, 5.0))
#plt.yticks(np.arange(-11, 12, 1.0))
plt.legend()
plt.grid(b=True, which='major', axis='both')
plt.show()
