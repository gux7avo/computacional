#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 21:09:25 2022

@author: gustavo
"""

from moduloDiferencias import dif_adelante_h2, dif_central_puntos, dif_atras_h2

alfa = [0., 5., 10., 15., 20., 25., 30.]
beta = [1.6595, 1.5434, 1.4186, 1.2925, 1.1712, 1.0585, 0.9561]
h = 0.087266


# -------- Cálculo de las derivadas en los extremos y puntos centrales

izquierda = 25 * dif_adelante_h2(beta[0], beta[1], beta[2], h)
print(izquierda)

for i in range(1, len(alfa)-1):
    aproximacion = dif_central_puntos(beta[i-1], beta[i+1], h)
    velocidad = 25 * aproximacion
    print(velocidad)
    
derecha = 25 * dif_atras_h2(beta[-1], beta[-2], beta[-3], h)
print(derecha)