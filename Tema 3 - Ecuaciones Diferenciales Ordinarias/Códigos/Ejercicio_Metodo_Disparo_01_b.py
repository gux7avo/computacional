from metodosDirectos import integraorden4
from scipy import optimize
import numpy as np

def condIni(u):
    return np.array([0.0, u])

def r(u):
    X, Y = integraorden4(F, xInicio, condIni(u), xAlto, h)
    y = Y[len(Y) - 1]
    r = y[0] - 1.0
    
    return r

def F(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -3.0 * y[0] * y[1]
    
    return F

xInicio = 0.0
xAlto = 2.0
h = 0.1

# Primer intento de CI desconocida
u1 = 1.0
X1, Y1 = integraorden4(F, xInicio,condIni(u1), xAlto, h)

# Primer intento de CI desconocida
u2 = 2.0
X2, Y2 = integraorden4(F, xInicio,condIni(u2), xAlto, h)

# Valor de CI interpolada
u = optimize.ridder(r, u1, u2)
X3, Y3 = integraorden4(F, xInicio,condIni(u), xAlto, h)