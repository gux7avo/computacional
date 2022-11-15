#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import potenciaInversa5
import numpy as np

def Bv(v):
    n = len(v)
    z = np.zeros(n)
    z[0] = 2.0 * v[0] - v[1]
    
    for i in range(1, n-1):
        z[i] = -v[i-1] + 2.0 * v[i] - v[i+1]
        z[n-1] = -v[n-2] + 2.0 * v[n-1]
    
    return z

n = 100
d = np.ones(n) * 6.0
d[0] = 5.0
d[n-1] = 7.0
e = np.ones(n-1) * (-4.0)
f = np.ones(n-2) * 1.0

lam, x = potenciaInversa5(Bv, d, e, f)

print('PLˆ2/EI = {0:}'.format(lam*(n+1)**2))


