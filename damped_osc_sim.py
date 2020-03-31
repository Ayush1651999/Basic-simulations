import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

omega = 2
P = 2*pi/omega   # P is the time period
dt = P/4000
T = 10*P
N = int(round(T/dt))
print(N)
t = np.linspace(0, N*dt, N+1)

m=1
c=2.5
k=1

y = np.zeros(N+1)
x = np.zeros(N+1)
# t= np.arange(N+1)

y[0] = 0
x[0] = 10

for n in range(N):
	x[n+1] = x[n] + y[n]*dt
	y[n+1] = y[n] + dt*(-c*y[n]/m - k*x[n]/m)
	

plt.plot(t,x)
plt.show()