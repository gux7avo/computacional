#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np

def f(x, y):
    f = np.zeros(2)
    f[0] = y[1]
    f[1] = -0.1 * y[1] - x
    return f

x = 0.0
xAlto = 2.0
y = np.array([0., 1.])
h = 0.05

X, Y = euler(f, x, y, xAlto, h)

s_Exacta = 100. * X - 5. * X**2 + 990. *(np.exp(-0.1 * X) - 1.)

