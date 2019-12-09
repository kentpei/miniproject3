import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
# frequency is the number of times a wave repeats a second
frequency = 1000
num_samples = 48000
# The sampling rate of the analog to digital convert
sampling_rate = 48000.0
amplitude = 16000
file = "test.wav"
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]
nframes = num_samples
comptype = "NONE"
compname = "not compressed"
nchannels = 1
sampwidth = 2
wav_file = wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))
frame_rate = 48000.0
infile = "test.wav"
num_samples = 48000
wav_file = wave.open(infile, 'r')
data = wav_file.readframes(num_samples)
wav_file.close()
data = struct.unpack('{n}h'.format(n=num_samples), data)
data = np.array(data)
data_fft = np.fft.fft(data)
#print(data_fft[:8])
freq = np.abs(data_fft)
data_fft = np.fft.fft(sine_wave)
#print(abs(data_fft[1000]))
#print("Max frequency is {} HZ".format(np.argmax(freq)))
'''
plt.subplot(2,1,1)
plt.plot(data[:600])
plt.title("Original audio wave dia")
plt.subplot(2,1,2)
plt.plot(freq)
plt.title("Frequencies found")
plt.xlim(0,1200)
plt.show()
'''
noisy_freq = 50
sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/  sampling_rate) for x1 in range(num_samples)]
sine_noise = np.array(sine_noise)
