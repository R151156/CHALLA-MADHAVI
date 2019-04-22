import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,10,0.01)
x=np.cos(2*np.pi*t)
plt.plot(t,x)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show( )