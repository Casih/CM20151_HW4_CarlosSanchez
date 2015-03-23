
# coding: utf-8

# In[99]:

import scikits.audiolab as audio
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
import matplotlib.pylab as plt
import numpy as np 


sampling_rate, input_signal = wavfile.read('miaudio.wav')
print("sampling rate = {} Hz, length = {} samples, channels = {}".format(sampling_rate, *input_signal.shape))
print(input_signal[50000:50010])
time_array = np.arange(0, len(input_signal)/float(sampling_rate), 1/float(sampling_rate))
input_signal = input_signal/1e9
dt = 1 / (sampling_rate * len(input_signal)/4.)
n = len(input_signal)
from scipy.fftpack import fft, fftfreq
fft_x = fft(input_signal) / n 
freq = fftfreq(n, dt) 
fft_x_shifted = np.fft.fftshift(fft_x)
freq_shifted = np.fft.fftshift(freq)

#Los Armonicos se encontraron haciendo una convolucion con una distribucion normal en ese pedazo.

plt.figure(figsize=(20,20))
half_n = np.ceil(n/2.0)
fft_x_half = (2.0) * fft_x[:half_n]
freq_half = freq[:half_n]
ampl = np.abs(fft_x_half)
plt.plot(freq_half/1e9,ampl*100000)
plt.title("Armonicos en 'Carlos' con mi voz", fontsize =28)
plt.xlabel("Frecuencia (Hz)", fontsize =28)
plt.ylabel("Amplitud", fontsize =28)
plt.annotate('Primer armonico ~ 0.2',xy=(0.2,3.7), xytext=(0.01,3.8),fontsize=10,arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Segundo armonico ~ 0.3',xy=(0.32,3.2), xytext=(0.01,3.6),fontsize=10,arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Tercer armonico ~ 0.45',xy=(0.45,2.2), xytext=(0.01,3.4),fontsize=10,arrowprops=dict(facecolor='black', shrink=0.05))
plt.savefig('mivoz_fft.png')