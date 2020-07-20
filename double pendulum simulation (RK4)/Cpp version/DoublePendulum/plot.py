# =============================================================================
# 
# 
#  =============================================================================
#  Simulating the double pendulum using Runge–Kutta method(RK4)
#  =============================================================================
# 
# Updated on Mon Jul 20 2020
# @author: Ahmed Alkharusi
# =============================================================================


import numpy as np
import matplotlib.pyplot as plt

r1 = 1 # These should match with the .cpp file
r2 = 1

pendulum2_theta_matrix= np.loadtxt('Pendulum2_results.txt', usecols=range(2))
pendulum1_theta_matrix= np.loadtxt('Pendulum1_results.txt', usecols=range(2))

pendulum2_theta = pendulum2_theta_matrix[:,1]
pendulum1_theta = pendulum1_theta_matrix[:,1]

pendulum1_x = r1*np.sin(pendulum1_theta)
pendulum1_y = - r1*np.cos(pendulum1_theta)

pendulum2_x = r2*np.sin(pendulum2_theta) + pendulum1_x
pendulum2_y = pendulum1_y - r2*np.cos(pendulum2_theta)

scatter_x = []
scatter_y = []
counter = 0
save_every_n_frames = 50

for j in range(int(len(pendulum1_y)/save_every_n_frames)):
    i = j*save_every_n_frames
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-4,4), ylim=(-2.2, 2.2))
    ax.set_facecolor('k')
    x = [0, pendulum1_x[i]]
    y = [0, pendulum1_y[i]]
    ax.plot(x,y,lw=3,color='deepskyblue')
    x1 = [pendulum1_x[i], pendulum2_x[i]]
    y1 = [pendulum1_y[i], pendulum2_y[i]]
    scatter_x.append(pendulum2_x[i])
    scatter_y.append(pendulum2_y[i])
    ax.plot(x1,y1,'o-',lw=3,color='deepskyblue',markersize=10)
    ax.scatter(scatter_x,scatter_y,lw=0.0005,alpha=0.11,color='w')
    ax.set_xlabel('$x-Axis$',fontsize=12)
    ax.set_ylabel('$y-Axis$',fontsize=12)
    ax.set_title('Double pendulum simulation (RK4 method)',fontsize=14)
    #ax.grid()
    #fig.savefig(str(j)+'.png',dpi=600)
    plt.show()