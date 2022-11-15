#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np

s = np.array([[3.0, 1.0, 4.0],
              [1.0, 7.0, 2.0],
              [4.0, 2.0, 0.0]])

v = np.array([1.0, 1.0, 1.0])

for i in range(100):
	vAnterior = v.copy()
	z = np.dot(s,v)
	zMag = np.sqrt(np.dot(z,z))
	v = z/zMag
    
	if np.dot(vAnterior,v) < 0.0:
		sign = -1.0
		v = -v
	else: sign = 1.0
    
	if np.sqrt(np.dot(vAnterior - v, vAnterior - v)) < 1.0e-6: break

lam = sign*zMag

print('Total de iteraciones es: {0:}'.format(i))

print('El eigenvalor es: {0:}'.format(lam))