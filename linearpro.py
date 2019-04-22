import matplotlib.pyplot as mp
import numpy as np
import cmath as m
x=[1,2,3,1]
y=[1,2,3,1]
j=m.sqrt(-1)
X=[]
Y=[]
Z=[]
for n in range(0,len(x)):
	s1=0
	for k in range(0,(len(x)-1)):
		s1=s1+(x[k]*np.exp(-j*2*np.pi*k*n/4))
	X=np.append(X,s1)
print(X)
for m in range(0,(len(y)-1)):
                 s2=0
                 for l in range(0,(len(y)-1)):
                               s2=s2+(x[l]*np.exp(-j*2*np.pi*l*m/4))
                 Y=np.append(Y,s2)
print(Y)
z=x+y
for p in range(0,(len(z)-1)):
                 s3=0
                 for q in range(0,(len(z)-1)):
                           s3=s3+(x[q]*np.exp(-j*2*np.pi*q*p/4))
                 r=np.append(r,S3) 
print(r)    
mp.plot(X)
mp.subplot(311)
mp.plot(Y)
mp.subplot(312)
mp.plot(r)
mp.subplot(313)
mp.show()

	