#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""


from prettytable import PrettyTable
import numpy as np

def f(x, y):
    f = np.zeros(1)
    f[0] = np.sin(y)
    return f

x = 0.0
xAlto = 0.5
y = np.array([1.])
h = 0.1

tabla = PrettyTable()


X, Y = integraorden2(f, x, y, xAlto, h)

for i in range(len(X)):
    tabla.add_row(['%1.1f' % X[i],'%1.8f' % Y[i]])

