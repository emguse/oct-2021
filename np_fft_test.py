import numpy as np
import matplotlib.pyplot as plt

N = 256
dt = 0.01
f1, f2 = 10, 20
t = np.arange(0, N*dt, dt)
freq = np.linspace(0, 1.0/dt, N)

f = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t) + 0.3 *np.random.randn(N)

f_fft = np.fft.fft(f)

amp = np.abs(f_fft)

fig = plt.figure()
plt.subplots_adjust(wspace=0.4)
plt.subplot(121)
plt.plot(t, f, label='f(n)')
plt.xlabel("Time", fontsize=16)
plt.ylabel("Sig", fontsize=16)
plt.grid()
plt.legend(loc=1, fontsize=16)
plt.subplot(122)
plt.plot(freq, amp, label='|F(k)|')
plt.xlabel('Freq', fontsize=16)
plt.ylabel('Amplitude', fontsize=16)
plt.grid()
plt.legend(loc=1, fontsize=16)
plt.show()
fig.savefig("fig_fft.png")