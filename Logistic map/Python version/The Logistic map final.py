# -*- coding: utf-8 -*-
"""
The logistic map
Created on Tue Jul 14  2020

@author: Ahmed Alkharusi
"""
import time
import matplotlib.pyplot as plt
import numpy as np
start_time = time.time()

def logistic_map(current_population,fertility, max_iteration):
    result = np.array([])
    result = np.append(result,current_population)  
    if fertility < critical_point :
        temp = max_iteration
        max_iteration = 200
        for i in range(max_iteration-1):
            current_population = fertility * current_population* (1-current_population)   
            result = np.append(result,current_population)

        for i in range(temp-max_iteration):#check
            result = np.append(result,result[max_iteration-1])   
    else:
        for i in range(max_iteration-1):
            current_population = fertility * current_population* (1-current_population)   
            result = np.append(result,current_population)
    return result

def results_matrix(fertility,max_iteration):
    result_matrix=np.zeros([fertility.size,max_iteration])

    for i in range(fertility.size):
        result_matrix[:,i] = logistic_map(current_population,fertility[i],max_iteration)
    return result_matrix
#Global
critical_point = 3.6
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Parameters

current_population = 0.5
max_iteration = 1000
fertility = np.linspace(2.8,4,1000)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Plot
fig = plt.figure()  
ax = fig.add_subplot(111)
res=results_matrix(fertility,max_iteration)
iteration_number = 100

for i,j in enumerate(fertility):    
    ax.scatter(np.full((1,fertility.size-iteration_number),j),res[:,i][iteration_number:],color='black',s=0.001,alpha=0.5)
 
plt.show()
print(" %s seconds " % (time.time() - start_time))

