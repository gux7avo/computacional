#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np
import random

def intMC(f, a, b, n):
    s = 0

    for i in range(n):
        x = random.uniform(a, b)
        s += f(x)
        
    I = (float(b-a)/n) * s

    return I

def intvecMC(f, a, b, n):
    x = np.random.uniform(a, b, n)
    s = np.sum(f(x))
    I = (float(b-a)/n) * s

    return I

def int2MC(f, a, b, n):
    # se guardan las aproximaciones intermedias de la integral en el arreglo I,
    # donde I[k-1] es k veces la funcion evaluada
    s = 0

    I = np.zeros(n)

    for k in range(1, n+1):
        x = np.random.uniform(a, b)
        s += f(x)
        I[k-1] = (float(b-a)/k) * s
    return I

def int3MC(f, a, b, n, N=100):
    s = 0
    Ivalores = []
    kvalores = []
    
    for k in range(1, n+1):
        x = np.random.uniform(a, b)
        s += f(x)
        if k % N == 0:
            I = (float(b-a)/k) * s
            Ivalores.append(I)
            kvalores.append(k)
    
    return kvalores, Ivalores

def intareaMC(f, a, b, n, m):
    porDebajo = 0 
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            porDebajo += 1
    area = porDebajo/float(n) * m * (b - a)
    
    return area

def intareavecMC(f, a, b, n, m):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, m, n)
    porDebajo = np.sum(y < f(x))
    area = porDebajo/float(n) * m * (b - a)
    
    return area

def int3areaMC(f, a, b, n, m, N=1000):
    Ivalores = []
    kvalores = []
    porDebajo = 0
    
    for k in range(1, n+1):
        x = np.random.uniform(a, b)
        y = np.random.uniform(0, m)
        
        if y <= f(x):
            porDebajo += 1
        
        area = porDebajo/float(k) * m * (b-a)
        
        if k % N == 0:
            I = area
            Ivalores.append(I)
            kvalores.append(2 * k)
    
    return kvalores, Ivalores

