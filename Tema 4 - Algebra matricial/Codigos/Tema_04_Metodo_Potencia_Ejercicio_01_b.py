#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np

s = # Agrega el arreglo

v = # Aca va el otro arreglo

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
