import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

T = 20
dt = T/200
N = int(round(T/dt))
t = np.linspace(0, N*dt, N+1)
print(t)

H=I=V = np.zeros(N+1)

H[0] = 1000
I[0] = 0
V[0] = 100

for n in range(N):
	H[n+1] = H[n] + dt*(10**5 - 0.1*H[n] - (2**(-7))*H[n]*V[n])
	I[n+1] = I[n] + dt*((2**(-7))*H[n]*V[n] - 0.5*I[n])
	V[n+1] = V[n] + dt*(-(2**(-7))*H[n]*V[n] - 5*V[n] + 100*I[n])

plt.plot(t,I)
plt.show()