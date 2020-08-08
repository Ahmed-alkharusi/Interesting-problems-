"""
Plots
====================
=Snadpiles=
====================
Created on Aug 8 2020
@author : Ahmed Al-kharusi
"""


import numpy as np
import matplotlib.pyplot as plt

n = 401 #this should match with the points_no in the Source.cpp file
matrix= np.loadtxt('result.txt', usecols=range(n))
matrix[int((n-1)/2)][int((n-1)/2)]=0
matrix = - matrix
plt.tick_params(axis='both',which='both',
bottom=False,
top=False, 
left=False, 
right=False,   
labelbottom=False,
labeltop=False,
labelleft=False,
labelright=False)
plt.imshow(matrix, cmap ='magma')

plt.savefig('result_.png', dpi=300)