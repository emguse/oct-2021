import numpy as np
from scipy.fft import fft, fftfreq, ifft # scipy.fftpack is Legacy
from scipy.signal.windows import hann
import matplotlib.pyplot as plt

N = 256 # Number of samples
dt = 0.01 #Sampling time
fq1, fq2 = 5, 40 # Generation frequency
fc = 20 # cutoff frequency
A1, A2 = 20, 5 # amplification
t = np.arange(0, N*dt, dt) # time axis

# Waveform generation
f1 = A1 * np.sin(2*np.pi*fq1*t)
f2 = A2 * np.sin(2*np.pi*fq2*t)
wf = f1 + f2

# plot
plt.figure(figsize=(12.8, 4.8))
plt.subplot(111)
plt.plot(t, wf)
plt.xlabel('Time [s]')
plt.ylabel("Signal")

# fast-fourier-transform
fs = fft(wf)
freq = fftfreq(N, d=dt)

# plot
plt.figure(figsize=(12.8, 14.4))
plt.subplot(311)
plt.title("Real part")
plt.plot(fs.real)
plt.subplot(312)
plt.title("Imaginary part")
plt.plot(fs.imag)
plt.subplot(313)
plt.title("Frequency")
plt.plot(freq)
plt.xlabel('Number of data')
plt.show()

# Normalize
fsa = np.abs(fs/(N/2))
fsa[0] = fsa[0]/2
fsa = fsa[:int(N/2)]
p_freq = fftfreq(N, d=dt)[:N//2]

# fast-fourier-transform with hannimg window
fw = hann(N)
fsh = fft(fw * wf)
# Normalize
fsha = np.abs(fsh/(N/2))
fsha[0] = fsha[0]/2
fsha = fsha[:int(N/2)]
# Compensate for the effect of the window function on power
cf = 1/(sum(fw)/N) # hanning window amplitude correction factor
fshc = cf * fft(fw * wf)
fshca = np.abs(fshc/(N/2))
fshca[0] = fshca[0]/2
fshca = fshca[:int(N/2)]

# plot
plt.figure(figsize=(12.8, 4.8))
plt.subplot(111)
plt.plot(p_freq, fsa, label='without hanning')
plt.plot(p_freq, fsha, label='with hanning')
plt.plot(p_freq, fshca, label='with corrected hanning')
plt.legend()
plt.xlabel('Frequency [Hz]')
plt.ylabel("amplitude")
plt.show()

# Duplicate the array
fs2 = fs.copy()
# Low-pass filter (sets the signal above the cutoff frequency "fc" to zero)
fs2[(freq > fc)] = 0
# revers-fast-fourier-transform
#wf2 = ifft(fs2)
# Normalizing
fs2 = np.abs(fs2/(N/2))
fs2[0] = fs2[0]/2
fs2 = fs2[:int(N/2)]
# revers-fast-fourier-transform
#wf2 = wf2 * N
#wf2 = wf.real

# plot
plt.figure(figsize=(12.8, 9.6))
plt.subplot(211)
plt.plot(p_freq, fs2, label='filterd')
plt.legend()
plt.xlabel('Frequency [Hz]')
plt.ylabel("amplitude")
#plt.subplot(212)
#plt.plot(t, wf2, label='filterd')
#plt.legend()
#plt.xlabel('time [s]')
#plt.ylabel("signal")
plt.show()
