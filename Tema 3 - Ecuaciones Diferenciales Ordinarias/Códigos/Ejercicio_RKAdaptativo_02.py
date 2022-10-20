#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:59:48 2022

@author: gustavo
"""

from metodosDirectos import integra_RKAdaptativo
import numpy as np
import matplotlib.pyplot as plt

def F(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -4.75 * y[0] - 10.0 * y[1]
    return F

x = 0.0
xAlto = 10.0
y = np.array([-9.0, 0.0])
h = 0.1

X, Y = integra_RKAdaptativo(F, x, y, xAlto, h)

plt.plot(X, Y[:,0],'.-', X, Y[:,1],'.-r')
plt.title('Solución gráfica al problema')
plt.xlabel('x')
plt.legend(('y', 'dy/dx'), loc=0)
plt.grid(True)
plt.savefig('Ejercicio_RKAdaptativo_02.png', format='png')
plt.show()