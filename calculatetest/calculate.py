import numpy as np
from scipy.integrate import quad

def f(a):
    fx=a**2*np.pi
    return fx

def g(x,a):
    gx=2*np.pi*x**2*(1-np.cos(a/x))
    return gx

def F(x,a):
    F=f(a)-g(x,a)
    return F

def l(x):
    l=np.sqrt(1-1/9*((2*x+1)**1.5-1)**2)*np.sqrt(2*x+1)
    return l*4

def n(r,k):
    n=4*np.pi*r**2/(np.sqrt(1-k*r**2))
    return n
def nn(r1,k):
    nn=quad(lambda r:n(r,k),0,r1)
    return nn[0]
