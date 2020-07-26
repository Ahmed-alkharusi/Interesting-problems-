"""
Plots
====================
=The Mandelbrot set=
====================
Created on Sat Jul 25 2020

@author : Ahmed Al-kharusi
"""


import numpy as np
import matplotlib.pyplot as plt

n = 2000 #this should match with the points_no in the Source.cpp file
matrix= np.loadtxt('results.txt', usecols=range(n))
plt.imshow(matrix, cmap ='magma')

plt.savefig('result.png', dpi=300)
