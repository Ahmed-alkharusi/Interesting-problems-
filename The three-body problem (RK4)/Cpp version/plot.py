
"""
=============================================================================
 Solving the three - body problem numerically using the RK4 (Plots)
 =============================================================================
Created on Jul 30 2020
@author: Ahmed Alkharusi
"""
import numpy as np
import matplotlib.pyplot as plt

obj1 = np.loadtxt("result_obj1.txt")
obj2 = np.loadtxt("result_obj2.txt")
obj3 = np.loadtxt("result_obj3.txt")
[ob_1_x,ob_1_y] = obj1.transpose()
[ob_2_x,ob_2_y] = obj2.transpose()
[ob_3_x,ob_3_y] = obj3.transpose()
print("Plotting ...")
planets_x = [ob_1_x, ob_2_x,ob_3_x]
planets_y = [ob_1_y, ob_2_y,ob_3_y]
planet_colors = ['w', 'gold','r']

save_every_n_frames = 4000

obj1_x_sacatter = []
obj2_x_sacatter = []
obj3_x_sacatter = []

obj1_y_sacatter = []
obj2_y_sacatter = []
obj3_y_sacatter = []


frame = 3
shift_y = 0
shift_x = 0
for j in range(int(len(ob_1_x)/save_every_n_frames)-1):
    i = j*save_every_n_frames
    fig = plt.figure(figsize=(16,9))
    avx = (ob_1_x[i] + ob_2_x[i] + ob_3_x[i])/3
    avy = (ob_1_y[i] + ob_2_y[i] + ob_3_y[i])/3
    ax = fig.add_subplot(111, autoscale_on=False,xlim=(avx-(16/9)*frame,avx+(16/9)*frame),ylim=(avy-frame,avy+frame))

    ax.set_facecolor('k')
    ax.scatter(ob_1_x[i],ob_1_y[i],lw=0.5,s=200,color='w')
    ax.scatter(ob_2_x[i],ob_2_y[i],lw=0.5,s=200,color='b')
    ax.scatter(ob_3_x[i],ob_3_y[i],lw=0.5,s=200,color='r')

    obj1_x_sacatter.append(ob_1_x[i])
    obj2_x_sacatter.append(ob_2_x[i])
    obj3_x_sacatter.append(ob_3_x[i])

    obj1_y_sacatter.append(ob_1_y[i])
    obj2_y_sacatter.append(ob_2_y[i])
    obj3_y_sacatter.append(ob_3_y[i])

    ax.scatter(obj1_x_sacatter,obj1_y_sacatter,s=1,alpha=0.7,color='w')
    ax.scatter(obj2_x_sacatter,obj2_y_sacatter,s=1,alpha=0.7,color='b')
    ax.scatter(obj3_x_sacatter,obj3_y_sacatter,s=1,alpha=0.7,color='r')

    ax.grid(color='w',alpha=0.05)
    fig.savefig('./figures/'+str(j)+'.png',dpi=300,bbox_inches='tight')
    plt.show(block=False)
    plt.close()
