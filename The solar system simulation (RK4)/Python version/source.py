"""
# =============================================================================
# Simulating the double pendulum using Runge–Kutta method (RK4)
# =============================================================================
Created on Tue Jul 21 2020
@author: Ahmed Alkharusi
"""
import numpy as np
import matplotlib.pyplot as plt

#initial conditions
# ----------------------N.B. in this simulation we are assuming that all the planets have the same mass-------------------------------
mercury_arr_x = np.array([ 0.384,0])
mercury_arr_y = np.array([0,10.090399])

venus_arr_x = np.array([ 0.72,0])
venus_arr_y = np.array([0,7.4203409])

earth_arr_x = np.array([ 0.996,0])
earth_arr_y = np.array([0,2*np.pi])

mars_arr_x = np.array([ 1.57,0])
mars_arr_y = np.array([0,4.9117598])

jupiter_arr_x = np.array([ 5.13,0])
jupiter_arr_y = np.array([0,2.80370840])

saturn_arr_x = np.array([ 8.99,0])
saturn_arr_y = np.array([0,2.1502124])

uranus_arr_x = np.array([ 19.1,0])
uranus_arr_y = np.array([0,1.441907])

neptune_arr_x = np.array([ 30,0])
neptune_arr_y = np.array([0,1.150996])

def deriv(planet_arr1,planet_arr2,t):
    return np.array([planet_arr1[1],-4*pow(np.pi,2)*planet_arr1[0]/(pow(pow(planet_arr1[0],2)+pow(planet_arr2[0],2),1.5))])#pow((pow(planet_arr1[0],2)+pow(planet_arr2[0],2)),1.5)

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

def implement_rk4(earth_arr_x,earth_arr_y,t,h,steps_no):
    time_arr = np.array([t])
    func_array1 = np.array([earth_arr_x])
    func_array2 = np.array([earth_arr_y])

    for i in range(steps_no):
        temp =earth_arr_x
        (t,earth_arr_x) = rk4(deriv,earth_arr_x,earth_arr_y,t,h)
        t -=h
        (t,earth_arr_y) = rk4(deriv,earth_arr_y,temp,t,h)
        time_arr = np.append(time_arr, t)
        func_array1 = np.vstack((func_array1,np.array([earth_arr_x])))
        func_array2 = np.vstack((func_array2,np.array([earth_arr_y])))
    [x, vx] = func_array1.transpose()
    [y, vy] = func_array2.transpose()
    return [(x,y),time_arr]

t = 0 # starting time
h = 1/(10000) # step size for the RK4 method
steps_no = 1000000 # number of steps of the RK4 method

[(x_mercury, y_mercury),time_arr] = implement_rk4(mercury_arr_x,mercury_arr_y,t,h,steps_no)
(x_venus, y_venus) = implement_rk4(venus_arr_x,venus_arr_y,t,h,steps_no)[0]
(x_earth, y_earth) = implement_rk4(earth_arr_x,earth_arr_y,t,h,steps_no)[0]
(x_mars, y_mars) = implement_rk4(mars_arr_x,mars_arr_y,t,h,steps_no)[0]
(x_jupiter, y_jupiter) = implement_rk4(jupiter_arr_x,jupiter_arr_y,t,h,steps_no)[0]
(x_saturn, y_saturn) = implement_rk4(saturn_arr_x,saturn_arr_y,t,h,steps_no)[0]
(x_uranus, y_uranus) = implement_rk4(uranus_arr_x,uranus_arr_y,t,h,steps_no)[0]
(x_neptune, y_neptune) = implement_rk4(neptune_arr_x,neptune_arr_y,t,h,steps_no)[0]



planets_x = [x_mercury, x_venus, x_earth, x_mars, x_jupiter, x_saturn, x_uranus, x_neptune]
planets_y = [y_mercury, y_venus, y_earth, y_mars, y_jupiter, y_saturn, y_uranus, y_neptune]
planet_colors = ['gray', 'gold', 'dodgerblue', 'chocolate','burlywood', 'palegoldenrod', 'lightskyblue', 'paleturquoise']

save_every_n_frames = 50

#(ymin, ymax) = (np.min(y_neptune),np.max(y_neptune))
#(xmin, xmax) = (np.min(x_neptune),np.max(x_neptune))
(ymin, ymax) = (-32,32)
(xmin, xmax) = (-32,32)


[x_mercury_scatter, x_venus_scatter, x_earth_scatter, x_mars_scatter, x_jupiter_scatter, x_saturn_scatter, x_uranus_scatter, x_neptune_scatter] = [[],[],[],[],[],[],[],[]]
[y_mercury_scatter, y_venus_scatter, y_earth_scatter, y_mars_scatter, y_jupiter_scatter, y_saturn_scatter, y_uranus_scatter, y_neptune_scatter] = [[],[],[],[],[],[],[],[]]
planets_x_scatter = [x_mercury_scatter, x_venus_scatter, x_earth_scatter, x_mars_scatter, x_jupiter_scatter, x_saturn_scatter, x_uranus_scatter, x_neptune_scatter]
planets_y_scatter = [y_mercury_scatter, y_venus_scatter, y_earth_scatter, y_mars_scatter, y_jupiter_scatter, y_saturn_scatter, y_uranus_scatter, y_neptune_scatter]
time_arr = np.round(time_arr,1)

for j in range(int(len(x_neptune)/save_every_n_frames)):
    i = j*save_every_n_frames
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(xmin, xmax), ylim=(ymin, ymax))
    ax.set_facecolor('k')
    ax.scatter(0,0,lw=1,s=5,color='yellow')
    color_counter=0
    for x,y in zip(planets_x, planets_y):
        if color_counter<4:
            ax.scatter(x[i],y[i],lw=0.5,s=5,color=planet_colors[color_counter])
        else:
            ax.scatter(x[i],y[i],lw=0.5,s=50,color=planet_colors[color_counter])
        color_counter+=1
        for x1,y1 in zip(planets_x_scatter, planets_y_scatter):
            x1.append(x[i])
            y1.append(y[i])
            ax.scatter(x1,y1,s=0.1,alpha=0.011,color='w')


    ax.text(xmin+(0.45* 17.42), ymin+(0.2* 17.42), "Time: "+str(time_arr[i])+ " yrs", ha="center", va="center",size=10,backgroundcolor = 'w',fontsize=10,alpha=0.8)
    ax.set_xlabel('$x-Axis$ $(AU)$',fontsize=12)
    ax.set_ylabel('$y-Axis$ $(AU)$',fontsize=12)
    ax.set_title('The solar system simulation (RK4 method)',fontsize=14)
    ax.grid(color='w',alpha=0.05)
    fig.savefig(str(j)+'.png',dpi=300)
    plt.show()
    #plt.close()
"""
# =============================================================================
# Please check the answers!!!
# =============================================================================
References:
#Implementing the RK4 method in Python
https://youtu.be/mqoqAovXxWA
by Prof. Niels Walet
"""
