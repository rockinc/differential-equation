"""
Simpson method is for calculating integrals
"""

import numpy as np

def simpson_integral(mode,x1,x2,dev,func):
    xlist = np.linspace(x1,x2,dev)
    dx = (x2-x1)/dev
    area = 0
    if mode==0:
        for i in range(dev):
            area += func(xlist[i])*dx
    elif mode==1:
        for i in range(dev-1):
            area += (func(xlist[i])+func(xlist[i+1]))*dx/2
    elif mode==2:
        for i in range(dev-2):
            area += (func(xlist[i])+4*func(xlist[i])+func(xlist[i+2]))*dx/6
    else:
        raise(NotImplementedError)
    return area

# define some functions
def gauss(x):
    return np.exp(-1*x**2)

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

print(simpson_integral(mode=2,x1=-100,x2=100,dev=1001,func=gauss)) #sqrt(pi)
print(simpson_integral(mode=2,x1=0,x2=np.pi,dev=100001,func=cos)) #0