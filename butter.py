import matplotlib.pyplot as plt
import numpy as np
import math 
wp=float(input("enter the pass band frequency"))
ws=float(input("enter the stop band frequency"))
dp=float(input("enter the gain in db"))
ds=float(input("enter the gain in db"))
a=dp*dp
b=ds*ds
x=-1+float(1/a)
y=-1+float(1/b)
print(x)
print(y)
m=float(y/x)
k=math.log10(m)
l=math.log10(float(ws/wp))
print(k)
print(l)
c=float(k/l)
N=(0.5)*c
print(N)
d=math.ceil(N)
print(d)
r=float(1/a)
s=float(1/2*d)
t=(r-1)**s
wc=wp/t
print(wc)
w=np.arange(0,1000,10)
i=w/wc
q=2*d
j=1+(i**q)
g=j**0.5
h=1/g
plt.subplot(211)
plt.plot(w,h)
s=(2*k)-1
I=complex(0,1)
w=np.linspace(-np.pi,np.pi,1000)
T=float(input("enter the sampling interval"))
C=wc*d
G=float(d/2)
A=float((d-1)/2)
print(A)
print(G)
J=I*w/T
sum=1
if(d%2==0):
              for k in range(1,G,1):
                      B=2*np.sin(s*np.pi/q)
                      H=(J**2)+b*wc*J+wc**2
                      sum=sum*H
                      M=C/sum
                      print(B)
else:
              for k in range(1,int(A),1):
                      B=2*np.sin(s*np.pi/q)
                      H=(J**2)+b*wc*J+wc**2
                      sum=sum*H
                      Q=sum*(J+wc)
                      M=C/Q
                       print(B)
plt.subplot(212)
plt.plot(w,M)
plt.show( )