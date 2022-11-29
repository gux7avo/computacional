#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

data01 = np.loadtxt('Poisson.txt', delimiter='\t', skiprows=1)

X, Y, Z = data01[:,0], data01[0:,1], data01[:,2]

fig = plt.figure()

ax.plot_trisurf(X, Y, Z, cmap=plt.cm.jet, lw=0.1)
ax.tricontourf(X, Y, Z, zdir='z', offset=-1, cmap=plt.cm.coolwarm)

ax.view_init(30, 45)
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Solución a la ec. de Poisson en 2D')
plt.show()