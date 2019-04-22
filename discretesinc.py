import matplotlib.pyplot as plt
import numpy as np
t=np.arange(-10,10,0.10)
x=np.sinc(2*np.pi*t)
plt.stem(t,x)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show( )