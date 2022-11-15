#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np
from random import random


def choleski(a):
    n = len(a)
    
    for k in range(n):
        try:
            a[k,k] = np.sqrt(a[k,k] - np.dot(a[k,0:k], a[k,0:k]))
        except ValueError:
            err('La matriz no es definida positiva')
        
        for i in range(k+1, n):
            a[i,k] = (a[i,k] - np.dot(a[i,0:k], a[k,0:k]))/a[k,k]
    
    for k in range(1,n): a[0:k,k] = 0.0
    
    return a

def LUdescomp(a):
    n = len(a)
    
    for k in range(0, n-1):
        for i in range(k+1, n):
           if a[i,k] != 0.0:
               lam = a [i,k]/a[k,k]
               a[i,k+1:n] = a[i,k+1:n] - lam * a[k,k+1:n]
               a[i,k] = lam
    return a

def LUsoluc(a,b):
    n = len(a)
    
    for k in range(1, n):
        b[k] = b[k] - np.dot(a[k,0:k],b[0:k])
        
    b[n-1] = b[n-1]/a[n-1,n-1]    
    
    for k in range(n-2,-1,-1):
       b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    
    return b

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

def jacobi(a, tol = 1.0e-8):
    
    def umbral(a):
        suma = 0.0

        for i in range(n-1):
            for j in range(i+1, n):
                suma = suma + abs(a[i, j])
    
        return 0.5*suma/n/(n-1) 

    def rotacion(a, p, k, l): # Rotacion para hacer a[k,l] = 0
        aDiff = a[l,l] - a[k,k]
        
        if abs(a[k,l]) < abs(aDiff) * 1.0e-36: t = a[k,l]/aDiff
        else:
            phi = aDiff/(2.0 * a[k,l])
            t = 1.0/(abs(phi) + np.sqrt(phi**2 + 1.0))
            
            if phi < 0.0: t = -t
        
        c = 1.0/np.sqrt(t**2 + 1.0); s = t*c
        tau = s/(1.0 + c)
        temp = a[k,l]
        a[k,l] = 0.0
        a[k,k] = a[k,k] - t * temp
        a[l,l] = a[l,l] + t * temp
        
        for i in range(k): # Caso i < k
            temp = a[i,k]
            a[i,k] = temp - s * (a[i,l] + tau * temp)
            a[i,l] = a[i,l] + s * (temp - tau * a[i,l])
        
        for i in range(k+1, l):  # Caso k < i < l
            temp = a[k,i]
            a[k,i] = temp - s * (a[i,l] + tau * a[k,i])
            a[i,l] = a[i,l] + s * (temp - tau * a[i,l])
        
        for i in range(l+1, n):  # Caso i > l
            temp = a[k,i]
            a[k,i] = temp - s * (a[l,i] + tau * temp)
            a[l,i] = a[l,i] + s *(temp - tau * a[l,i])
        
        for i in range(n):  # Actualizacion matriz de transformacion
            temp = p[i,k]
            p[i,k] = temp - s * (p[i,l] + tau * p[i,k])
            p[i,l] = p[i,l] + s * (temp - tau * p[i,l])
    
    n = len(a)
    p = np.identity(n, float)
    
    for k in range(20):
         mu = umbral(a) # Calcula un nuevo umbral
         
         for i in range(n-1):  # Barrido en la matriz
            for j in range(i+1, n):
                if abs(a[i,j]) >= mu:
                    rotacion(a, p, i, j)
    
         if mu <= tol: return np.diagonal(a), p
    
    print('El método de Jacobi no converge')
    
def swapRenglon(v, i, j):
    v.setflags(write=True)
    if len(v.shape) == 1:
        v[i], v[j] = v[j] , v[i]
    else:
        v[[i,j],:] = v[[j,i],:]
        
def swapColumna(v, i, j):
    # v.setflags(write=True)
    v[:,[i,j]] = v[:,[j,i]]
    
def ordenaJacobi(lam, x):
    n = len(lam)
    
    for i in range(n-1):
        index = i
        val = lam[i]
        
        for j in range(i+1, n):
            if lam[j] < val:
                index = j
                val = lam[j]
        
        if index != i:
            swapRenglon(lam, i, index)
            swapColumna(x, i, index)
            
def formaEstd(a, b):

    def invierte(L): # Invierte una matriz L
        n = len(L)
        
        for j in range(n-1):
            L[j,j] = 1.0/L[j,j]
            
            for i in range(j+1,n):
                L[i,j] = -np.dot(L[i,j:i],L[j:i,j])/L[i,i]
        
        L[n-1,n-1] = 1.0/L[n-1,n-1]
        
    n = len(a)
    L = choleski(b)          
    invierte(L)
    h = np.dot(b,np.inner(a,L))
    return h, np.transpose(L)

def potenciaInversa(a, s, tol=1.0e-6):
    n = len(a)
    aAst = a - np.identity(n) * s  # Forma [a*] = [a] - s[I]
    aAst = LUdescomp(aAst)       # Descompone [a*]
    x = np.zeros(n)
    
    for i in range(n):          # Semilla [x] para los numeros aleatorios
        x[i] = random()
        
    xMag = np.sqrt(np.dot(x,x)) # Normaliza [x]
    x =x/xMag
    
    for i in range(50):         # Comienzan las iteraciones
        xAnterior = x.copy()         # Guarda el actual [x]
        x = LUsoluc(aAst, x)      # Resuelve [a*][x] = [xOld]
        xMag = np.sqrt(np.dot(x,x)) # Normaliza [x]
        x = x/xMag
        
        if np.dot(xAnterior,x) < 0.0:  # Detecta cambio de signo de [x]
            sign = -1.0
            x = -x
        else: sign = 1.0
        
        
        if np.sqrt(np.dot(xAnterior - x, xAnterior - x)) < tol:
            return s + sign/xMag, x, i
    
    print('El método de la potencia inversa no converge')  
        
def potenciaInversa5(Bv, d, e, f, tol=1.0e-6):
    
    n = len(d)
    d, e, f = LUdescomp5(d, e, f)
    x = np.random.rand(n)
    xMag = np.sqrt(np.dot(x,x))
    x = x/xMag
    
    for i in range(30):
        xAnterior = x.copy()
        x = Bv(xAnterior)
        x = LUsoluc5(d, e, f, x)
        xMag = np.sqrt(np.dot(x,x))
        x = x/xMag
        
        if np.dot(xAnterior,x) < 0.0:
            sign = -1.0
            x = -x
        else: sign = 1.0
        
        if np.sqrt(np.dot(xAnterior - x,xAnterior - x)) < tol:
            return sign/xMag, x
    
    print('El método de la potencia inversa no converge')
    
def householder(a):
    n = len(a)
    
    for k in range(n-2):
        u = a[k+1:n,k]
        uMag = np.sqrt(np.dot(u,u))
        
        if u[0] < 0.0: uMag = -uMag
        
        u[0] = u[0] + uMag
        h = np.dot(u,u)/2.0
        v = np.dot(a[k+1:n,k+1:n],u)/h
        g = np.dot(u,v)/(2.0*h)
        v = v - g * u
        a[k+1:n,k+1:n] = a[k+1:n,k+1:n] - np.outer(v,u)- np.outer(u,v)
        a[k,k+1] = -uMag
        
    return np.diagonal(a), np.diagonal(a,1)

def calculaP(a):
        
    n = len(a)
    p = np.identity(n) * 1.0
    
    for k in range(n-2):
        u = a[k+1:n,k]
        h = np.dot(u,u)/2.0
        v = np.dot(p[1:n,k+1:n],u)/h
        p[1:n,k+1:n] = p[1:n,k+1:n] - np.outer(v,u)
    
    return p