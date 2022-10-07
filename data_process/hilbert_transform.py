#這是一個hilbert_transform的測試程式
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp

duration = 1.0
fs = 400.0
samples = int(fs*duration)

t = np.arange(samples) / fs

#https://vimsky.com/zh-tw/examples/usage/python-scipy.signal.chirp.html
signal = chirp(t, 20 ,  1, 100.0)
signal *= (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t))

#https://vimsky.com/zh-tw/examples/usage/python-scipy.signal.hilbert.html
analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)

plt.plot(t, signal, label='signal')
plt.plot(t, amplitude_envelope, label='envelope')
plt.show()