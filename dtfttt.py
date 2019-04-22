import numpy as np
import matplotlib.pyplot as mp
import cmath as m
x=[6,4,5,3,2,3]
j=m.sqrt(-1)
X=[]
W=np.linspace(-np.pi,np.pi,1000)
for i in range(0,1000):
	s=0
	for n in range(0,len(x)):
		s=s+(x[n]*np.exp(-n*W[i]*j))
	X.append(s)
mp.subplot(2,1,1)
mp.plot(W,np.abs(X))
mp.title("magnitude spectrum")
mp.xlabel("frequency")
mp.ylabel("magnitude")
mp.subplot(2,1,2)
mp.plot(W,np.angle(X))
mp.title("phase spectrum")
mp.xlabel("frequency")
mp.ylabel("phase in rad")
mp.show()


