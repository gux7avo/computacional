#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import potenciaInversa
import numpy as np

a = #Aqui va el arreglo

s = 5.0

lam, x, i = potenciaInversa(a, s)

print('Número de iteraciones: {0:}'.format(i))
print('\nEl eigenvalor es: {0:}'.format(lam))
print('\nEl eigenvector es: \n {0:}'.format(x))
