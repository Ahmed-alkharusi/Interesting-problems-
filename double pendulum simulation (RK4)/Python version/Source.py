"""
# =============================================================================
# Simulating the double pendulum using Runge–Kutta method (RK4)
# =============================================================================

Created on Fri Jul 17 2020
@author: Ahmed Alkharusi
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
# =============================================================================
# globals
# =============================================================================
m1 = 1   #mass of the 1st pendulum 
m2 = 1    #mass of the 2nd pendulum   
g = 10 #gravity
r1 = 1  #length of the 1st pendulum   
r2 = 1   #length of the 2nd pendulum
x = y = []
# =============================================================================
# Functions defn.
# =============================================================================

def angular_acc1(a1_arr,a2_arr):
    """Calculate the angular acceleration for the 1st pendulum
        Inputs-> a1_arr: np.array([Initial angle, Initial angular velocity]);
                 a2_arr: np.array([Initial angle, Initial angular velocity]);"""
    num = -g *(2*m1+m2)*np.sin(a1_arr[0]) - m2*g*np.sin(a1_arr[0]-2*a2_arr[0])- 2* m2*np.sin(a1_arr[0]-a2_arr[0]) * (r2*pow(a2_arr[1],2)+r1*pow(a1_arr[1],2)*np.cos(a1_arr[0]-a2_arr[0]))
    den = r1*(2*m1+m2-m2 * np.cos(2*a1_arr[0]-2*a2_arr[0]))
    return num/den

def angular_acc2(a1_arr,a2_arr):
    """Calculate the angular acceleration for the 2nd pendulum
        Inputs-> a1_arr: np.array([Initial angle, Initial angular velocity]);
                 a2_arr: np.array([Initial angle, Initial angular velocity]);"""
    temp = (2*np.sin(a1_arr[0]-a2_arr[0])) 
    num = temp * (r1*pow(a1_arr[1],2)*(m1+m2)+g*(m1+m2)*np.cos(a1_arr[0])+r2*pow(a2_arr[1],2)*m2*np.cos(a1_arr[0]-a2_arr[0]))
    den = r2*(2*m1+m2-m2 * np.cos(2*a1_arr[0]-2*a2_arr[0]))
    return num/den

def deriv_a1(a1_arr,a2_arr,t):
    """
    Returns an array np.array([first derivative, 2nd derivative])
    Inputs-> a1_arr: np.array([Initial angle, Initial angular velocity]);
             a2_arr: np.array([Initial angle, Initial angular velocity]);
             t: the dependent variable;
    """
    return np.array([a1_arr[1],angular_acc1(a1_arr,a2_arr)])

def deriv_a2(a2_arr,a1_arr,t):
    return np.array([a2_arr[1],angular_acc2(a1_arr,a2_arr)])

def rk4(deriv,func_i,func_i2, x_i,h):
    """
    Implements the RK4 method
    Inputs-> deriv: a function that takes two arguments;
             func_i: the function to be calculated;
             func_i2: this is just passed as an argument for func_i (see above deriv_a1 and deriv_a2);
             x_i: the dependent variable of func_i;
             h: the step size;
             
    """
    k1 = deriv(func_i,func_i2,x_i)
    k2 = deriv(func_i+h/2,func_i2,h*k1/2)
    k3 = deriv(func_i+h/2,func_i2,h*k2/2)
    k4 = deriv(func_i+h,func_i2,h*k3)
    func = func_i + (1/6) * h * (k1 +2*k2+2*k3+k4)
    x = x_i + h
    return (x,func)

# =============================================================================
# def init(): #Uncomment these for the animation
#     line.set_data([], [])
#     time_text.set_text('')
#     return line, time_text
# 
# def animate(i):
#     x = [0, pendulum1_x[i], pendulum2_x[i]]
#     y = [0, pendulum1_y[i], pendulum2_y[i]]
#     
#     line.set_data(x,y)
#     #time_text.set_text(time_template % (i*h)) #Uncomment this to display the time in the animated plot
#     return line, time_text
# 
# =============================================================================
# =============================================================================
# The results
# =============================================================================
    
#Initial conditions ([initial angle, initail angular speed])
a1_arr = np.array([np.pi/2,0])
a2_arr = np.array([np.pi/2,1])
t = 0 # starting time
h = 0.001 # step size for the RK4 method
steps_no = 100000 # number of steps of the RK4 method
time_arr = np.array([t])
func_array1 = np.array([a1_arr])
func_array2 = np.array([a2_arr])

for i in range(steps_no):
    temp =a1_arr
    (t,a1_arr) = rk4(deriv_a1,a1_arr,a2_arr,t,h)
    t =-h 
    (t,a2_arr) = rk4(deriv_a2,a2_arr,temp,t,h)
    time_arr2 = np.append(time_arr, t)
    func_array1 = np.vstack((func_array1,np.array([a1_arr])))
    func_array2 = np.vstack((func_array2,np.array([a2_arr])))
 
# You can plot the pendulum's position or angular speed/acceleration as a function of time
[pendulum1_theta, pendulum1_angular_speed] = func_array1.transpose()
[pendulum2_theta, pendulum2_angular_speed] = func_array2.transpose()

pendulum1_x = r1*np.sin(pendulum1_theta)
pendulum1_y = - r1*np.cos(pendulum1_theta)

pendulum2_x = r2*np.sin(pendulum2_theta) + pendulum1_x
pendulum2_y = pendulum1_y - r2*np.cos(pendulum2_theta)


# Here I used the matplotlib template of the double pendulum animation to animate the plot
# =============================================================================
# fig = plt.figure()
# ax = fig.add_subplot(111, autoscale_on=False, xlim=(-3.9, 3.9), ylim=(-2, 2))
# ax.set_xlabel('$x-Axis$',fontsize=12)
# ax.set_ylabel('$y-Axis$',fontsize=12)
# ax.set_title('Double pendulum simulation (RK4 method)',fontsize=14)
# ax.grid()
# 
# line, = ax.plot([], [], 'o-',lw=3,color='mediumvioletred',markersize=15)
# time_template = 'time = %0.1fs'
# time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
# 
# ani = animation.FuncAnimation(fig, animate, np.arange(1, len(pendulum1_y)),
#                               interval=0, blit=True, init_func=init)
# 
# #ax.scatter(pendulum2_x, pendulum2_y,s=5, color='black',alpha=0.5)
# #ani.save('double_pendulum_200.avi', fps=20, dpi =8)
# plt.show()
# =============================================================================
# =============================================================================
# #Save each frame separately
# =============================================================================
scatter_x = []
scatter_y = []
counter = 0
save_every_n_frames = 25
for j in range(int(len(pendulum1_y)/save_every_n_frames)):
    i = j*save_every_n_frames
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-4,4), ylim=(-2.1, 2.1))
    x = [0, pendulum1_x[i]]
    y = [0, pendulum1_y[i]]
    ax.plot(x,y,lw=3,color='mediumvioletred')
    x1 = [pendulum1_x[i], pendulum2_x[i]]
    y1 = [pendulum1_y[i], pendulum2_y[i]]
    scatter_x.append(pendulum2_x[i])
    scatter_y.append(pendulum2_y[i])
    ax.plot(x1,y1,'o-',lw=3,color='mediumvioletred',markersize=15)
    ax.scatter(scatter_x,scatter_y,lw=0.0005,color='black')
    ax.set_xlabel('$x-Axis$',fontsize=12)
    ax.set_ylabel('$y-Axis$',fontsize=12)
    ax.set_title('Double pendulum simulation (RK4 method)',fontsize=14)
    ax.grid()
    fig.savefig(str(j)+'.png',dpi=600)
    plt.show()

"""
# =============================================================================
# Please check the answers!!!
# =============================================================================
References:

#Implementing the RK4 method in Python 
https://youtu.be/mqoqAovXxWA
by Prof. Niels Walet  

#The formulas for the angular acceleration 
https://www.myphysicslab.com/pendulum/double-pendulum-en.html
    
#Animating the double pendulum (N.B. the implementation used here is different)
https://matplotlib.org/3.2.1/gallery/animation/double_pendulum_sgskip.html
"""






