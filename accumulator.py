import numpy as np
n=int(input("enter number of samples:"))
x=[]
for i in range(n):
	y=int(input("enter the samples:"))
	x=np.append(x,y)
print("entered samples are:",x)
y=[]
sum=0
for i in range(n):
	sum=sum+x[i]
	y=np.append(y,sum)
print("accumulator output is:",y)


