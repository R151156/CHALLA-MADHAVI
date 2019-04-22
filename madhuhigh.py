import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('madhu.wav')
print(fs)
print(data)
t=np.arange(0,len(data)/fs,1.0/fs)
plt.plot(t,data[0:len(t)])
plt.show( )
wav.write('madhu_high.wav',5*fs,data)



