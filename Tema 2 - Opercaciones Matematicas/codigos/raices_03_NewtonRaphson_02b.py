# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""

from moduloRaices import buscaraiz, newtonRaphson2
import numpy as np
import matplotlib.pyplot as plt

def f(x): return np.sin(x) + 3 * np.cos(x) - 2

def df(x): return np.cos(x) - 3 * np.sin(x)

intervalo1 = []
intervalo2 = []

inicio, final, dx = -2., 2. , 0.01

# Se determina el intervalo para la primera raíz
a1, b1 = buscaraiz(f, inicio, final, 0.1)
print('Una raiz esta en el intervalo ({0:1.4f}, {1:1.4f})'.format(a1, b1))
intervalo1.append(a1)
intervalo1.append(b1)

# Se determina el intervalo para la segunda raíz
inicio = b1
a2, b2 = buscaraiz(f, inicio, final, 0.1)
print('Otra raiz esta en el intervalo ({0:1.4f}, {1:1.4f})'.format(a2, b2))
intervalo2.append(a2)
intervalo2.append(b2)

# Se ocupa la ver. 2.0 del algoritmo MNR
raiz1 = newtonRaphson2(f, df, intervalo1[0], intervalo1[-1], 1.e-4)
print('La primera raiz en el intervalo ({0:1.4f}, {1:1.4f}) = {2:1.5f}'.format(intervalo1[0], intervalo1[-1], raiz1))

# Se ocupa la ver 2.0 del algoritmo MNR
raiz2 = newtonRaphson2(f, df, intervalo2[0], intervalo2[-1], 1.e-4)
print('La segunda raiz en el intervalo ({0:1.4f}, {1:1.4f}) = {2:1.5f}'.format(intervalo2[0], intervalo2[-1], raiz2))

x = np.linspace(-2, 2)

plot1 = plt.figure(1)
plt.plot(x, f(x))

plot2 = plt.figure(2)
plt.plot(x, f(x), color='g')
plt.plot(raiz1, 0, 'ro', label='Raiz 1 = ' + str(round(raiz1, 3)))
plt.plot(raiz2, 0, 'bo', label='Raiz 2 = ' + str(round(raiz2, 3)))

plt.show()