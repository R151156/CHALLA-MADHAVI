import matplotlib.pyplot as plt
import numpy as np
import cmath as math
m=int(input("enter the input value"))
N=[]
Y=[]
Z=[]
P=[]
X=[]
V=[]
Q=[]
for n in range(0,m-1):
                  w1=1
                  N.append(w1)
plt.subplot(1,5,1)
plt.stem(N)
a=int((m-1)/2)
b=int((m-3)/2)
for n in range(0,a):
	e=(2*n)/(m-1)	
	Y.append(e)
for n in range(b,m-1):
	d=1-((2*n)/(m-1))
	Y.append(d)
plt.subplot(1,5,2)
plt.stem(Y)
for n in range(0,m-1):
                  w3=0.5*(1-np.cos((2*np.pi*n)/m-1))
                  Z.append(w3)
plt.subplot(1,5,3)
plt.stem(Z)
al=0.54
for n in range(0,m-1):
                  w4=al-(1-al)*(np.cos((2*np.pi*n)/m-1))
                  X.append(w4)
plt.subplot(1,5,4)
plt.stem(X)
for n in range(0,m-1):
                  w5=0.4-0.5*(np.cos((2*np.pi*n)/m-1))-0.08*(np.cos((4*np.pi*n)/m-1))
                  X.append(w5)
plt.subplot(1,5,5)
plt.stem(X)
plt.show()