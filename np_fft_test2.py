import numpy as np
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
plt.subplot(121)
plt.plot(t, wf)
plt.xlabel('Time [s]')
plt.ylabel("Signal")
plt.subplot(122)
plt.xlim(0, 0.5)
plt.plot(t, wf)
plt.xlabel('Time [s]')
plt.ylabel("Signal")
plt.show()

# fast-fourier-transform
fs = np.fft.fft(wf)
freq = np.fft.fftfreq(N, d=dt)

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
fsa = fsa[1:int(N/2)]
p_freq = freq[1:int(N/2)]

#plot
plt.figure(figsize=(12.8, 4.8))
plt.subplot(111)
plt.plot(p_freq, fsa)
plt.show()