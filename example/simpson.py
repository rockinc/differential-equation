"""
Simpson method is for calculating integrals
"""

import numpy as np

def simpson_integral(array,mode:int,x1:float,x2:float)->float:
    dx = (x2-x1)/(len(array)-1)
    area = 0
    if mode==0:
        area = np.sum(array)*dx
    elif mode==1:
        for i in range(len(array)-1):
            area += (array[i]+array[i+1]) *dx/2
    elif mode==2:
        if len(array)>=3:
            list_coeff = [3-(-1)**i for i in range(len(array))]
            if len(array)%2==1:
                list_coeff[0],list_coeff[-1] = 1,1
            else:
                list_coeff[0],list_coeff[-2],list_coeff[-1] = 1,2.5,1.5
        elif len(array)==2:
            list_coeff = [1.5,1.5]
        elif len(array)==1:
            list_coeff = [3]
        else:
            raise(NotImplementedError)
        array_coeff = np.array(list_coeff)
        area = np.sum(array_coeff*array)*dx*2/6
    elif mode==3:
        unit = [2,3,3]
        if len(array)>=4:
            list_coeff = unit*((len(array)-1)//3)
            list_coeff[0]=1
            if len(array)%3==1:
                list_coeff+=[1]
            elif len(array)%3==2:
                list_coeff+=[7/3,4/3]
            else:
                list_coeff+=[17/9,32/9,8/9]
        elif len(array)==1:
            list_coeff = [8/3]
        elif len(array)==2:
            list_coeff = [4/3,4/3]
        elif len(array)==3:
            list_coeff = [8/9,32/9,8/9]
        else:
            raise(NotImplementedError)
        array_coeff = np.array(list_coeff)
        area = np.sum(array_coeff*array)*dx*3/8
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