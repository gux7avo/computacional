# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""
from moduloRaices import newtonRaphson1
import numpy as np

def f(x): return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752

def df(x): return 4.0*x**3 - 19.2*x**2 + 12.9*x + 20.538

raiz, numIter = newtonRaphson1(2.0, f, df)

print('La raíz es = {0:1.5f}'.format(raiz))
print('Número de iteraciones realizadas = {0:}'.format(numIter))

x = np.linspace(0, 5)

# Aquí va la rutina de graficación
# No olvides llamar a las correspondientes librerías