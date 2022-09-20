# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:25:43 2013

@author: Gustavo
"""

from moduloDiferencias import ddif_central
import numpy as np

def funcion(x):
    return np.exp(-x)

def error_rel(exacta, aprox):
    pass

h = 0.64
x = 1.
exacta = 0.36787944

for i in range(1, 15):
    aprox = ddif_central(funcion, x, h)
    error = error_rel(exacta, aprox)
    print(h, aprox, error)
    h = h*0.5
