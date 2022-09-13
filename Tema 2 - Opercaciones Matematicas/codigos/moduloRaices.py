#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from math import ceil, log
import numpy as np


def buscaraiz(f, a, b, dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while f1*f2 > 0.0:
        if x1 >= b: return None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        return x1,x2

def biseccion(f, x1, x2, switch=0, tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0: return x1
    f2 = f(x2)
    if f2 == 0.0: return x2
    
    if f1*f2 > 0.0: print('La raiz no se ha identificado en un intervalo')

    n = ceil(log(abs(x2 - x1)/tol)/log(2.0))
    
    for i in np.arange(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        
        if (switch == 1) and (abs(f3) > abs(f1)) \
                        and (abs(f3) > abs(f2)):
            return None
        
        if f3 == 0.0: return x3
        
        if f2*f3 < 0.0:
            x1 = x3; f1 = f3
        else:
            x2 =x3; f2 = f3
    return (x1 + x2)/2.0

def newtonRaphson1(x, f, df, tol=1e-05):
    for i in range(50):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol: return x, i
    print('Son demasiadas iteraciones\n')

def newtonRaphson2(f, df, a, b, tol = 1.0e-9):
    fa = f(a)
    if fa == 0.0: return a

    fb = f(b)
    if f(b) == 0.0: return b

    if fa*fb > 0.0: print('La raiz no esta en el intervalo')
    x = 0.5 * (a + b)

    for i in range(30):
        fx = f(x)
        if abs(fx) < tol: return x

        if fa*fx < 0.0:
            b = x
        else:
            a = x; fa = fx

        dfx = df(x)
        
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x =  x + dx
        
        # Si el resultado esta fuera del intervalo
        # se usa el metodo de biseccion
        if (b - x)*(x - a) < 0.0:
            dx = 0.5*(b-a)
            x = a + dx
        
        if abs(dx) < tol*max(abs(b), 1.0): return x
    
    print('Son demasiadas iteraciones')
