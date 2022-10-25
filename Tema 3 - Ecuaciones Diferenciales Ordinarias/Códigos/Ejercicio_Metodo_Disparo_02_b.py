#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:54:08 2022

@author: gustavo
"""

from metodosDirectos import integra_RKAdaptativo
import numpy as np

def interpLineal(f, x1, x2):
    f1 = f(x1)
    f2 = f(x2)

    return x2 - f2 * (x2 - x1) / (f2 - f1)

def condIni(u):
    return np.array([0.0, 0.0, u])

def r(u):
    X, Y = integra_RKAdaptativo(F, xInicio, condIni(u), xAlto, h)
    y = Y[len(Y) - 1]
    r = y[0] - 2.0
    
    return r

def F(x, y):
    F = np.zeros(3)
    F[0] = y[1]
    F[1] = y[2]
    F[2] = 2.0 * y[2] + 6.0 * x * y[0]
    
    return F

xInicio = 5.0
xAlto = 0.0
u1 = 1.0
u2 = 2.0
h = -0.1

# Primer intento de CI desconocida
u1 = 1.0
X1, Y1 = integra_RKAdaptativo(F, xInicio, condIni(u1), xAlto, h)

# Primer intento de CI desconocida
u2 = 2.0
X2, Y2 = integra_RKAdaptativo(F, xInicio, condIni(u2), xAlto, h)

# Valor de CI interpolada
u = interpLineal(r, u1, u2)
X3, Y3 = integra_RKAdaptativo(F, xInicio, condIni(u), xAlto, h)