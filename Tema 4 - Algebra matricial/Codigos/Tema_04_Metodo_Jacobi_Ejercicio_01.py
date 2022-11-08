#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:31:23 2022

@author: gustavo
"""

from moduloMatrices import jacobi
import numpy as np

S = np.array([[ 80, 30, 0],
              [30, 40, 0],
              [0, 0, 60]])

lam, H = jacobi(S)

eje = len(lam)
eigenvalores = lam * np.eye(eje)

print('Esfuerzos principales')
print(eigenvalores)
print()
print('Eigenvectores')
print(H)