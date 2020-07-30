
"""
# =============================================================================
# Solving the three-body problem numerically using the RK4
# =============================================================================
Created on Jul 30 2020
@author: Ahmed Alkharusi
"""
import numpy as np
import matplotlib.pyplot as plt

#initial conditions
star1_arr_x = np.array([0.97000436,0.93240737/2])
star1_arr_y = np.array([-0.24308753,0.86473146/2])#white
m1 = 1

star2_arr_x = np.array([-0.97000436,0.93240737/2 ]) #blue
star2_arr_y = np.array([0.24308753,0.86473146/2])
m2 = 1

star3_arr_x = np.array([0,-0.93240737])#red
star3_arr_y = np.array([0,-0.86473146])
m3 = 1

obj_1 = np.array([star1_arr_x,star1_arr_y])
obj_2 = np.array([star2_arr_x,star2_arr_y])
obj_3 = np.array([star3_arr_x,star3_arr_y])



def deriv(obj_active, obj_passive1,mp1,obj_passive2,mp2):#no requred time argument
    v_x = obj_active[0][1]
    v_y = obj_active[1][1]

    xo = obj_active[0][0]
    yo = obj_active[1][0]

    xp1 = obj_passive1[0][0]
    yp1 = obj_passive1[1][0]

    xp2 = obj_passive2[0][0]
    yp2 =  obj_passive2[1][0]

    acc_x = -  ( ( mp1*( xo- xp1 )/pow(pow(xo-xp1,2)+pow(yo-yp1 ,2),3/2) ) + ( mp2*(xo -xp2 )/pow(pow(xo -xp2,2)+pow(yo-yp2,2),3/2)) )
    acc_y = -  ( ( mp1*( yo- yp1 )/pow(pow(xo-xp1,2)+pow(yo-yp1 ,2),3/2) ) + ( mp2*(yo -yp2 )/pow(pow(xo -xp2,2)+pow(yo-yp2,2),3/2)) )

    return np.array([[v_x,acc_x],[v_y,acc_y]])

def rk4(deriv,obj_active, obj_passive1,mp1,obj_passive2,mp2,h):
    k1 = deriv(obj_active    , obj_passive1,mp1,obj_passive2,mp2)
    k2 = deriv(obj_active+h/2, obj_passive1,mp1,obj_passive2,mp2)
    k3 = deriv(obj_active+h/2, obj_passive1,mp1,obj_passive2,mp2)
    k4 = deriv(obj_active+h  , obj_passive1,mp1,obj_passive2,mp2)
    func = obj_active + (1/6) * h * (k1 +2*k2+2*k3+k4)
    return func

def implement_rk4(obj_1,m1,obj_2,m2,obj_3,m3,t,h,steps_no):
    time_arr = np.array([t])
    result_obj_1 = np.array(obj_1)
    result_obj_2 = np.array(obj_2)
    result_obj_3 = np.array(obj_3)

    result_obj_1_x = result_obj_1[0]
    result_obj_1_y = result_obj_1[1]

    result_obj_2_x = result_obj_2[0]
    result_obj_2_y = result_obj_2[1]

    result_obj_3_x = result_obj_3[0]
    result_obj_3_y = result_obj_3[1]

    for i in range(steps_no):
        temp1 = obj_1
        temp2 = obj_2
        obj_1 = rk4(deriv,obj_1, obj_2,m2 ,obj_3,m3 ,h)
        obj_2 = rk4(deriv,obj_2 , temp1,m1,obj_3,m3,h)
        obj_3 = rk4(deriv,obj_3 , temp1,m1,temp2,m2,h)
        t+=h
        time_arr = np.append(time_arr, t)
        result_obj_1_x = np.vstack((result_obj_1_x, obj_1[0]))
        result_obj_1_y = np.vstack((result_obj_1_y, obj_1[1]))
        result_obj_2_x = np.vstack((result_obj_2_x, obj_2[0]))
        result_obj_2_y = np.vstack((result_obj_2_y, obj_2[1]))
        result_obj_3_x = np.vstack((result_obj_3_x, obj_3[0]))
        result_obj_3_y = np.vstack((result_obj_3_y, obj_3[1]))

    [ob_1_x, ob_1_vx] = result_obj_1_x.transpose()
    [ob_1_y, ob_1_vy] = result_obj_1_y.transpose()
    [ob_2_x, ob_2_vx] = result_obj_2_x.transpose()
    [ob_2_y, ob_2_vy] = result_obj_2_y.transpose()
    [ob_3_x, ob_3_vx] = result_obj_3_x.transpose()
    [ob_3_y, ob_3_vy] = result_obj_3_y.transpose()

    return [   [[ob_1_x, ob_1_vx], [ob_1_y, ob_1_vy]],  [[[ob_2_x, ob_2_vx]], [[ob_2_y, ob_2_vy]]],  [[[ob_3_x, ob_3_vx]], [[ob_3_y, ob_3_vy]]]   ]

t = 0 # starting time
h = 1/(10000) # step size for the RK4 method
steps_no = 100000 # number of steps of the RK4 method


[   [[ob_1_x, ob_1_vx], [ob_1_y, ob_1_vy]],  [[[ob_2_x, ob_2_vx]], [[ob_2_y, ob_2_vy]]],  [[[ob_3_x, ob_3_vx]], [[ob_3_y, ob_3_vy]]]   ] = implement_rk4(obj_1,m1,obj_2,m2,obj_3,m3,t,h,steps_no)


print("Plotting ...")
save_every_n_frames = 300

obj1_x_sacatter = []
obj2_x_sacatter = []
obj3_x_sacatter = []

obj1_y_sacatter = []
obj2_y_sacatter = []
obj3_y_sacatter = []


frame = 2
shift_y = 0
shift_x = 0
for j in range(int(len(ob_1_x)/save_every_n_frames)-1):
    i = j*save_every_n_frames
    fig = plt.figure(figsize=(16,9))
    avx = (ob_1_x[i] + ob_2_x[i] + ob_3_x[i])/3
    avy = (ob_1_y[i] + ob_2_y[i] + ob_3_y[i])/3
    ax = fig.add_subplot(111, autoscale_on=False,xlim=(avx-(16/9)*frame,avx+(16/9)*frame),ylim=(avy-frame,avy+frame))

    ax.set_facecolor('k')
    ax.scatter(ob_1_x[i],ob_1_y[i],lw=0.5,s=500,color='w')
    ax.scatter(ob_2_x[i],ob_2_y[i],lw=0.5,s=500,color='b')
    ax.scatter(ob_3_x[i],ob_3_y[i],lw=0.5,s=500,color='r')

    obj1_x_sacatter.append(ob_1_x[i])
    obj2_x_sacatter.append(ob_2_x[i])
    obj3_x_sacatter.append(ob_3_x[i])

    obj1_y_sacatter.append(ob_1_y[i])
    obj2_y_sacatter.append(ob_2_y[i])
    obj3_y_sacatter.append(ob_3_y[i])

    ax.scatter(obj1_x_sacatter,obj1_y_sacatter,s=1,alpha=0.7,color='w')
    ax.scatter(obj2_x_sacatter,obj2_y_sacatter,s=1,alpha=0.7,color='b')
    ax.scatter(obj3_x_sacatter,obj3_y_sacatter,s=1,alpha=0.7,color='r')

    #ax.set_xlabel('$x-Axis$ $(AU)$',fontsize=12)
    #ax.set_ylabel('$y-Axis$ $(AU)$',fontsize=12)
    ax.grid(color='w',alpha=0.05)
    fig.savefig('./figures/'+str(j)+'.png',dpi=300,bbox_inches='tight')
    plt.show(block=False)
    plt.close()
"""
# =============================================================================
# Please check the answers!!!
# =============================================================================
References:
#Implementing the RK4 method in Python
https://youtu.be/mqoqAovXxWA
by Prof. Niels Walet

#for the initial conditions see
https://doi.org/10.1093/pasj/psy057
and
https://arxiv.org/abs/math/0011268

"""
