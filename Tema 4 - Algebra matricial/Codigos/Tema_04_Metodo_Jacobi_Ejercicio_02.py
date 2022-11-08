#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:19:39 2022

@author: gustavo
"""

from moduloMatrices import formaEstd, jacobi, ordenaJacobi
import numpy as np

A = np.array([[1/3, -1/3, 0.0],
              [-1/3, 4/3, -1.0],
              [0.0, -1.0, 2.0]])

B = np.array([[1.0, 0.0, 0.0],
              [0.0, 1.0, 0.0],
              [0.0, 0.0, 2.0]])

H, T = formaEstd(A, B)

lam, Z = jacobi(H)

X = np.dot(T, Z)

ordenaJacobi(lam, X)

for i in range(3):
    X[:,i] = X[:,i]/np.sqrt(np.dot(X[:,i],X[:,i]))
    
print('Eigenvalores: {0:}\n'.format(lam))
print('Eigenvectores: {0:}\n'.format(X))