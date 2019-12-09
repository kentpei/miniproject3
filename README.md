# miniproject3_DSP
Create Easy filter using python and some research about FIR filter
Easy filter
-----
Library:	 
Matplotlib, wave, numpy.
First, create Sine signal with frequency of 1000HZ, amplitude of 16000, sampling rate of  48000, and pack the data with hexadecimal format so it produce 16 bit audio test.wav. Later, to check the frequency of radio, we unpack it 
to readable format like binary. So we use FFT to get all the frequencies. Later we plot the diagram below.
<img src="https://github.com/kentpei/miniproject3/blob/master/create_signal.png" width="50%" height="50%">
Second, we create sine noise and add it with original sine wave to create new signal. Clearly as we can see, original sin wave becomes messy and from combinedfrequency.png we can see we have one more frequency of 50. Later we create a low pass filter to eliminate the noise which help us get the original signal. And from After_filtering.png we can see the change of Frequency.
<img src="https://github.com/kentpei/miniproject3/blob/master/with_noise.png" width="50%" height="50%">
<img src="https://github.com/kentpei/miniproject3/blob/master/recover_signal.png" width="50%" height="50%">



