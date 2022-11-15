#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import potenciaInversa
import numpy as np

a = np.array([[ 11.0, 2.0,  3.0,  1.0,  4.0],
              [  2.0, 9.0,  3.0,  5.0,  2.0],
              [  3.0, 3.0, 15.0,  4.0,  3.0],
              [  1.0, 5.0,  4.0, 12.0,  4.0],
              [  4.0, 2.0,  3.0,  4.0, 17.0]])

s = 5.0

lam, x, i = potenciaInversa(a, s)

print('Número de iteraciones: {0:}'.format(i))
print('\nEl eigenvalor es: {0:}'.format(lam))
print('\nEl eigenvector es: \n {0:}'.format(x))
