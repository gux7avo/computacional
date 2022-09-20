# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:20:33 2013

@author: Gustavo
"""

# ------- Aproximaciones para puntos xi, yi

def dif_central_puntos(fh1, fh2, h):
    valor = (fh2 - fh1) / (2 * h)
    return valor

# ------- Aproximaciones para funciones dadas

def dif_central(f, x, h):
    valor = (f(x + h) - f(x - h))/(2 * h)
    return valor
    
def dif_adelante(f, x, h):
    valor = (f(x + h) - f(x))/h
    return valor

def dif_atras(f, x, h):
    valor = (f(x) - f(x + h))/h
    return valor

def seg_aprox_dif_adelante(f, x, h):
    valor = (-f(x + (2 * h)) + 4 * f(x + h) - 3 * f(x))/(2 * h)
    return valor

def ddif_central(f, x, h):
    valor = (f(x + h) - 2 * f(x) + f(x - h))/(h**2)
    return valor

# -------- Aproximaciones de orden O(h^{2})

def dif_adelante_h2(f0, f1, f2, h):
    valor = (- 3 * f0 + 4 * f1 - f2)/(2 * h)
    return valor

def dif_atras_h2(f0, f1, f2, h):
    valor = (3 * f0 - 4 * f1 + f2)/(2 * h)
    return valor
