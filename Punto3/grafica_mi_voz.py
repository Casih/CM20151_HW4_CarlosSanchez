
# coding: utf-8

import scikits.audiolab as audio
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
import matplotlib.pylab as plt
import numpy as np



sampling_rate, input_signal = wavfile.read('miaudio.wav')
#print("sampling rate = {} Hz, length = {} samples, channels = {}".format(sampling_rate, *input_signal.shape))
#print(input_signal[50000:50010])


time_array = np.arange(0, len(input_signal)/float(sampling_rate), 1/float(sampling_rate))


plt.figure()
plt.plot(time_array, input_signal/1e9)
plt.xlabel("tiempo(s)", fontsize=20)
plt.ylabel("Amplitud", fontsize=20)
plt.savefig("mi_voz.png")
