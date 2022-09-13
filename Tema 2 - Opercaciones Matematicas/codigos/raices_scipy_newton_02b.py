# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:53:20 2017

@author: Master Chief
"""

import scipy.optimize
import numpy as np

def f(x):
    y = x + 2 * np.cos(x)
    return y
    
raiz= scipy.optimize.newton(f,  2, fprime=lambda x: 1 - 2 * np.sin(x))

print('La raíz de la función es = {0:1.5f}'.format(raiz))

x = np.linspace(-5, 5)