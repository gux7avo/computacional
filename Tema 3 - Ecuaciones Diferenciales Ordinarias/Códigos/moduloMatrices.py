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
