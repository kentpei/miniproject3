'''
# proposed Gaussian distribution
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series
from random import gauss
white_noise = [gauss(0.0, 1.0) for i in range(10000)]
white_noise_series = Series(white_noise)
white_noise_series.hist()
plt.show()
plt.close()
import pyaudio
import numpy as np
import scipy.signal as signal

from random import gauss

CHUNK = 64 #the block size
Q = 50

pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paFloat32,
                            channels=1,
                            rate=44100,
                            output=True)

noise = [gauss(0.0, 1.0) for i in range(CHUNK)] # create gaussian distribution for white noise
b,a = signal.iirfilter(1,[2*500*(1-1/(2*Q))/44100,2*500*(1+1/(2*Q))/44100])
output = signal.lfilter(b,a,noise)
output.astype(np.float32)
#output = output.tobytes()
#stream.write(output)
plt.plot(output)
plt.title("out")
plt.show()
'''
# -*- coding: utf-8 -*-
import scipy.signal as signal
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

# parameters of FIR filter
a = np.array([1.0, -1.947463016918843, 0.9555873701383931])
b = np.array([0.9833716591860479, -1.947463016918843, 0.9722157109523452])
t = np.arange(0, 0.5, 1/44100.0)
x= signal.chirp(t, f0=10, t1 = 0.5, f1=1000.0)
# one time filter to x
y = signal.lfilter(b, a, x)
plt.subplot(2, 1, 1)
plt.plot(y)
plt.title("onetime")
x2 = x.reshape((-1,50))
z = np.zeros(max(len(a),len(b))-1, dtype=np.float)
y2 = []
for tx in x2:
    # filter to every single signal
    ty, z = signal.lfilter(b, a, tx, zi=z)
    y2.append(ty)
y2 = np.array(y2) #switch lst to array
y2 = y2.reshape((-1,))
print(np.sum((y-y2)**2)) # output magrin of error of two parameters
plt.subplot(2, 1, 2)
plt.plot(y2)
plt.title("separate")
pl.show()
pl.close()