import matplotlib.pyplot as plot
import numpy as np
fs=int(input("enter the sampling frequency"))
f1=int(input("enter the first frequency"))
f2=int(input("enter the second frequency"))
n=int(input("enter the sample rate"))
p1=int(input("enter the first phase"))
p2=int(input("enter the second phase"))
x=np.arange(n)
x1=np.cos(2*np.pi*f1/fs*x+p1)
plot.subplot(3,1,1)
plot.plot(x,x1)
plot.title('cos1')
plot.xlabel('samples')
plot.ylabel('amplitude')
x2=np.sin(2*np.pi*f2/fs*x+p2)
plot.subplot(3,1,2)
plot.plot(x,x2)
plot.title('sin1')
plot.xlabel('samples')
plot.ylabel('amplitude')
y=x1+x2
plot.subplot(3,1,3)
plot.plot(x,y)
plot.title('sampled output')
plot.show( )