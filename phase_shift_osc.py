import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

omega_1 = 2
omega_2 = 2.1
P = 2*pi/omega_1   # P is the time period
dt = P/4000
T = 5*P
N = int(round(T/dt))
print(N)
t = np.linspace(0, N*dt, N+1)


theta_1 = np.zeros(N+1)
theta_2 = np.zeros(N+1)
theta_3 = np.zeros(N+1)

theta_1[0] =1
theta_2[0] =2
theta_3[0] =3

for n in range(N):

	# next three lines are for getting positions, rest will stay the same
	if(n<N/2):
		theta_1[n+1] = theta_1[n] + (omega_1)*dt
		theta_2[n+1] = theta_2[n] + (omega_2)*dt
		theta_3[n+1] = theta_3[n] + (omega_1)*dt
		
	else:		
		theta_1[n+1] = theta_1[n] + (omega_1 + np.sin(theta_2[n]-theta_1[n]) + np.sin(theta_3[n]-theta_1[n]))*dt
		theta_2[n+1] = theta_2[n] + (omega_2 + np.sin(theta_1[n]-theta_2[n]) + np.sin(theta_3[n]-theta_2[n]))*dt
		theta_3[n+1] = theta_3[n] + (omega_1 + np.sin(theta_1[n]-theta_3[n]) + np.sin(theta_2[n]-theta_3[n]))*dt

	if(theta_1[n+1]>2*pi):
		theta_1[n+1] = theta_1[n+1]-2*pi
	if(theta_1[n+1]<0):
		theta_1[n+1] = theta_1[n+1]+2*pi

	if(theta_2[n+1]>2*pi):
		theta_2[n+1] = theta_2[n+1]-2*pi
	if(theta_2[n+1]<0):
		theta_2[n+1] = theta_2[n+1]+2*pi

	if(theta_3[n+1]>2*pi):
		theta_3[n+1] = theta_3[n+1]-2*pi
	if(theta_3[n+1]<0):
		theta_3[n+1] = theta_3[n+1]+2*pi


fig = plt.figure()
l1, l2, l3 = plt.plot(t, theta_1, 'b-', t, theta_2, 'r-', t, theta_3, 'g-')
fig.legend((l1, l2, l3), ('theta_1', 'theta_2', 'theta_3'), 'upper left')
fig.set_size_inches(18.5, 10.5)
plt.xlabel('t')
plt.show()