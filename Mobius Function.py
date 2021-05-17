
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
        div = after/ycor
        numsum += div
        y.append(numsum)

    return y

xlist=plotx(1000)
ylist=plotmoby(1000)
x = np.linspace(30,1000, 10000)
y = 1/np.sqrt(x)
y2 = -1/np.sqrt(x)
plt.plot(xlist, ylist, label = 'P(x)')
plt.plot(x,y,label = '1/sqrt(x)')
plt.plot(x,y2, label = '-1/sqrt(x)')


plt.xlabel('x')
#plt.xticks(np.arange(min(xlist)-1, max(xlist)+1, 1.0))
plt.yticks(np.arange(-1.0, 1.5, 0.5))
plt.legend()
plt.grid(b=True, which='major', axis='both')
plt.show()




