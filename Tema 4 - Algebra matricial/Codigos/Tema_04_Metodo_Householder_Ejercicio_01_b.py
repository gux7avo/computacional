#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import householder, calculaP
import numpy as np


a = # Aqui va el arreglo

d, c = householder(a)

print('Diagonal principal d: \n {0:}'.format(d))
print('\nSubdiagonal c: \n {0:}'.format(c))
print('\nMatriz de Transformación [P]: {0:}')
print(calculaP(a))