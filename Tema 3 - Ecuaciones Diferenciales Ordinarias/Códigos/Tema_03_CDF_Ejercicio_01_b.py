#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import LUdescomp3, LUsoluc3
import numpy as 

def ecuaciones(x, h, m):
    h2 = h * h
    d = np.ones(m+1) * (-2.0 + 4.0 * h2)
    c = np.ones(m)
    e = np.ones(m)
    b = np.ones(m+1) * 4.0 * h2 * x
    d[0] = 1.0
    e[0] = 0.0
    b[0] = 0.0
    c[m-1] = 2.0
    
    return c, d, e, b

xInicio = 0.0
xAlto = np.pi/2.0

m = 10


h = (xAlto - xInicio)/m
x = np.arange(xInicio, xAlto + h, h)

c, d, e, b = ecuaciones(x, h, m)

c, d, e = LUdescomp3(c, d, e)

y = LUsoluc3(c, d, e, b)

print("\n        x              y")

for i in range(m + 1):
    print('{:14.5e} {:14.5e}'.format(x[i], y[i]))
