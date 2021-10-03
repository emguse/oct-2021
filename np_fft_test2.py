import numpy as np
import matplotlib.pyplot as plt

N = 256 # Number of samples
dt = 0.01 #Sampling time
fq1, fq2 = 5, 40 # Generation frequency
fc = 20 # cutoff frequency
A1, A2 = 20, 5 # amplification
t = np.arange(0, N*dt, dt) # time axis
freq = np.linspace(0, 1.0/dt, N) # Frequency axis

# Waveform generation
f1 = A1 * np.sin(2*np.pi*fq1*t)
f2 = A2 * np.sin(2*np.pi*fq2*t)
wf = f1 + f2

# fast-fourier-transform
fs = np.fft.fft(wf)
#freq = np.fft.fftfreq(N, dt)
fsa = fs/(N/2) # Normalize the vertical axis.(Divide by N and double)
fsa[0] = fsa[0]/2 # Correct for DC component is not doubled

f_size = freq.size
fsb = np.delete(fsa, slice(int(f_size/2)-1, int(f_size)-1), None)
freq_niq = np.delete(freq, slice(int(f_size/2)-1, int(f_size)-1), None)

# Duplicate the array
fsa2 = fsa.copy()

# Low-pass filter (sets the signal above the cutoff frequency "fc" to zero)
fsa2[(freq > fc)] = 0

# revers-fast-fourier-transform
wf2 = np.fft.ifft(fsa2)
# Normalizing the amplitude scale
wf2 = np.real(wf2*N)

fig = plt.figure(figsize=(12.8, 4.8))
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.subplot(141)
plt.plot(t, wf)
plt.subplot(142)
plt.plot(freq, np.abs(fs))
plt.subplot(143)
plt.plot(freq, np.abs(fsa))
plt.subplot(144)
plt.plot(freq_niq, np.abs(fsb))
plt.show()
fig2 = plt.figure(figsize=(12.8, 4.8))
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.subplot(141)
plt.plot(t, wf2)
plt.subplot(142)
plt.plot(freq, np.abs(fsa2))
plt.show()