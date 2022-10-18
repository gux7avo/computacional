# -*- coding: utf-8 -*-
"""

@author: gusto
"""

import numpy as np

def euler(F, x, y, xAlto, h):
    X = []
    Y = []
    X.append(x)
    Y.append(y)

    while x < xAlto:
        h = min(h, xAlto - x)
        y = y + h * F(x, y)
        x = x + h
        X.append(x)
        Y.append(y)

    return np.array(X), np.array(Y)

def integraorden2(F, x, y, xAlto, h):

    def run_kut2(F, x, y, h):
        K0 = h * F(x, y)
        K1 = h * F(x + h/2., y + K0/2.)
        return  y + K1
    
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    
    while x < xAlto:
        h = min(h, xAlto - x)
        y = run_kut2(F, x, y, h)
        x = x + h
        X.append(x)
        Y.append(y)
    
    return np.array(X), np.array(Y)

def integraorden4(F, x, y, xAlto, h):

    def run_kut4(F, x, y, h):
        K0 = h * F(x, y)
        K1 = h * F(x + h/2., y + K0/2.)
        K2 = h * F(x + h/2., y + K1/2.)
        K3 = h * F(x + h, y + K2)
        
        return (K0 + 2. * K1 + 2. * K2 + K3) / 6.
    
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    
    while x < xAlto:
        h = min(h, xAlto - x)
        y = y + run_kut4(F, x, y, h)
        x = x + h
        X.append(x)
        Y.append(y)
    
    return np.array(X), np.array(Y)
