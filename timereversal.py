import matplotlib.pyplot as mp
import numpy as nm
n=int(input("enter the no of samples:"))
x=[]
for i in range(n):
	y=input("enter the samples:")
	x=nm.append(x,y)
print ("entered samples are:",x)
lenx=n
z=nm.zeros(lenx)
for i in range(lenx):
	if lenx-i>=0 and lenx-i<=lenx:
		z[i]=x[lenx-i-1]
print("timereversal ou[ut is:",z)
#print("time reversal of x[n] is:",y)


