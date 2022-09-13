# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:14:32 2020

@author: gusto
"""

from moduloRaices import buscaraiz
from scipy import optimize

def f(x):
    return (x**2 - 1)

a, b, dx = -2., 2., 0.1

intervalo1 = []
intervalo2 = []
raices = []

inicio = a
final = 0.

a1, b1 = buscaraiz(f, inicio, final, dx)

inicio = final
final = b
a2, b2 = buscaraiz(f, inicio, final, dx)

raiz1 = optimize.bisect(f, a1, b1)
raiz2 = optimize.bisect(f, a2, b2)

print('La raíz está en x = {0:1.6f}'.format(raiz1))
print('La raíz está en x = {0:1.6f}'.format(raiz2))

# Completa la rutina de graficación