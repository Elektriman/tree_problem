# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:51:17 2021

@author: Julien
"""


import cmath
import matplotlib.pyplot as plt
import numpy as np
from arithmetic import PPCM
from mpl_toolkits.mplot3d import Axes3D

P = []

N = 50
for i in range(-N, N):
    for j in range(-N, N):
        z = complex(i,j)
        z2 = z**2
        if z.real != 0 :
            P.append([int(abs(z2.real)), int(z2.imag), int(cmath.polar(z2)[0])])

X = np.array(P)[:,0]
Y = np.array(P)[:,1]
M = np.array(P)[:,2]


fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X,Y,M, marker='.')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')