#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from metodosDirectos import euler
from prettytable import PrettyTable
import numpy as np

def f(x, y):
    f = np.zeros(1)
    f[0] = x**2 - 4 * y
    return f

def s_Exacta(x):
    valor = (31/32.) * np.exp(-4*x) + (1/4.) * x**2 - (1/8.) *x + (1/32.)
    return valor

x = 0.0
xAlto = 0.03
y = np.array([1.])
h = 0.01

X, Y = euler(f, x, y, xAlto, h)

tabla = PrettyTable()


for i in range(1, len(Y)):
    diferencia = s_Exacta(X[i]) - Y[i]
    tabla.add_row([X[i], '%1.4f' % Y[i], '%1.4f' % s_Exacta(X[i]), '%1.4f:' % diferencia])

    