import matplotlib.pyplot as mp
import numpy as np
f1=int(input("enter the first frequency:"))
f2=int(input("enter the second frequency:"))
t=np.arange(0,10,0.02)
x1=np.sin(2*np.pi*f1*t)
mp.subplot(3,1,1)
mp.plot(t,x1)
mp.xlabel('---->time')
mp.ylabel('---->amplitude')
x2=np.sin(2*np.pi*f2*t)
mp.subplot(3,1,2)
mp.plot(t,x2)
z=x1+x2
mp.subplot(3,1,3)
mp.plot(t,z)
mp.title('result')
mp.show( )


