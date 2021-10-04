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
plt.subplot(111)
plt.plot(t, wf)
plt.xlabel('Time [s]')
plt.ylabel("Signal")

# fast-fourier-transform
fs = np.fft.fft(wf)
freq = np.fft.fftfreq(N, d=dt)

# Normalize
fsa = np.abs(fs/(N/2))
fsa[0] = fsa[0]/2
fsa = fsa[1:int(N/2)]
p_freq = freq[1:int(N/2)]

# fast-fourier-transform with hannimg window
fw = np.hanning(N)
fsh = np.fft.fft(fw * wf)
# Normalize
fsha = np.abs(fsh/(N/2))
fsha[0] = fsha[0]/2
fsha = fsha[1:int(N/2)]
# Compensate for the effect of the window function on power
cf = 1/(sum(fw)/N) # hanning window amplitude correction factor
fshc = cf * np.fft.fft(fw * wf)
fshca = np.abs(fshc/(N/2))
fshca[0] = fshca[0]/2
fshca = fshca[1:int(N/2)]

#plot
plt.figure(figsize=(12.8, 4.8))
plt.subplot(111)
plt.plot(p_freq, fsa, label='without hanning')
plt.plot(p_freq, fsha, label='with hanning')
plt.plot(p_freq, fshca, label='with corrected hanning')
plt.legend()
plt.xlabel('Frequency [Hz]')
plt.ylabel("amplitude")
plt.show()