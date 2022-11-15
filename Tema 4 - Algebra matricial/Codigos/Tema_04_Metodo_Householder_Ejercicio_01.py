#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import householder, calculaP
import numpy as np


a = np.array([[ 7.0, 2.0,  3.0, -1.0],
              [ 2.0, 8.0,  5.0,  1.0],
              [ 3.0, 5.0, 12.0,  9.0], 
              [-1.0, 1.0,  9.0,  7.0]])

d, c = householder(a)

print('Diagonal principal d: \n {0:}'.format(d))
print('\nSubdiagonal c: \n {0:}'.format(c))
print('\nMatriz de Transformación [P]: {0:}')
print(calculaP(a))