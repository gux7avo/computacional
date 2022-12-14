#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""


def LUdescomp3(c, d, e):
    n = len(d)
    for k in range(1, n):
        lam = c[k-1]/d[k-1]
        d[k] = d[k] - lam * e[k-1]
        c[k-1] = lam
        
    return c, d, e
    
def LUsoluc3(c, d, e, b):
    n = len(d)

    for k in range(1, n):
        b[k] = b[k] - c[k-1] * b[k-1]
        
    b[n-1] = b[n-1]/d[n-1]

    for k in range(n-2, -1, -1):
        b[k] = (b[k] - e[k] * b[k+1])/d[k]
    
    return b

def LUdescomp5(d, e, f):
    n = len(d)
    
    for k in range(n-2):
        lam = e[k]/d[k]
        d[k+1] = d[k+1] - lam * e[k]
        e[k+1] = e[k+1] - lam * f[k]
        e[k] = lam
        lam = f[k]/d[k]
        d[k+2] = d[k+2] - lam * f[k]
        f[k] = lam
        
    lam = e[n-2]/d[n-2]
    d[n-1] = d[n-1] - lam * e[n-2]
    e[n-2] = lam
    
    return d, e, f

def LUsoluc5(d, e, f, b):
    n = len(d)
    b[1] = b[1] - e[0] * b[0]
    
    for k in range(2, n):
        b[k] = b[k] - e[k-1] * b[k-1] - f[k-2] * b[k-2]
        
    b[n-1] = b[n-1]/d[n-1]
    b[n-2] = b[n-2]/d[n-2] - e[n-2] * b[n-1]
    
    for k in range(n-3, -1, -1):
        b[k] = b[k]/d[k] - e[k] * b[k+1] - f[k] * b[k+2]
    
    return b
