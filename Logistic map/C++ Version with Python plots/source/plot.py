"""
The logistic map
Created on Tue Jul 14  2020

@author: Ahmed Alkharusi
"""
import matplotlib.pyplot as plt
import numpy as np
max_iteration = 2000 #this must match with the .cpp file 
fertility= np.loadtxt('linspace.txt', usecols=range(max_iteration))
results = np.loadtxt('results.txt', usecols=range(max_iteration))

fig = plt.figure()  
ax = fig.add_subplot(111)
iteration_number = 100
for i,j in enumerate(fertility):    
    ax.scatter(np.full((1,fertility.size-iteration_number),j),results[:,i][iteration_number:],color='black',s=0.001,alpha=0.5)
#fig.savefig('result.pdf',dpi=100)
#fig.savefig('result.jpg',dpi=200)
plt.show()
