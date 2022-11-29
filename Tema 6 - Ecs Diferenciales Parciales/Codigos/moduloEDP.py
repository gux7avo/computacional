# -*- coding: utf-8 -*-

from math import fabs


def PoissonCero(u, x, y, nx, ny, eps, Func):

   itmax = 10000

   f = [[0]*(ny+1) for i in range(nx+1)]

   hx = (x[nx]-x[1])/(nx-1); kx = 1e0/(hx*hx)
   hy = (y[ny]-y[1])/(ny-1); ky = 1e0/(hy*hy) 
   kxy = 2e0*(kx + ky)

   for j in range(2,ny):
      for i in range(2,nx): f[i][j] = Func(x[i],y[j])

   for it in range(1,itmax+1):
      err = 0e0
      for j in range(2,ny):
         for i in range(2,nx):
            uij = (kx*(u[i-1][j] + u[i+1][j]) +
                   ky*(u[i][j-1] + u[i][j+1]) - f[i][j]) / kxy
            eij = 1e0 - u[i][j]/uij if uij else uij - u[i][j]
            if (fabs(eij) > err): err = fabs(eij)
            u[i][j] = uij

      if (err <= eps): break

   if (it >= itmax):
      print("PoissonCero: Se excedió el número máximo de iteraciones!"); return 1
   return 0

#----------------------------------------------------------------------------
def PoissonXY(u, x, y, nx, ny, eps, Func, CondX, CondY):
   itmax = 10000

   f = [[0]*(ny+1) for i in range(nx+1)]
   betXmin = [0]*(ny+1); betXmax = [0]*(ny+1)
   gamXmin = [0]*(ny+1); gamXmax = [0]*(ny+1)
   betYmin = [0]*(nx+1); betYmax = [0]*(nx+1)
   gamYmin = [0]*(nx+1); gamYmax = [0]*(nx+1)

   hx = (x[nx]-x[1])/(nx-1); kx = 1e0/(hx*hx)
   hy = (y[ny]-y[1])/(ny-1); ky = 1e0/(hy*hy) 
   kxy = 2e0*(kx + ky)

   for j in range(2,ny):
      for i in range(2,nx): f[i][j] = Func(x[i],y[j])
                                                        
   for i in range(1,nx+1):
      (alf_min,bet_min,gam_min,alf_max,bet_max,gam_max) = CondY(x[i])
      betYmin[i] = bet_min/(alf_min*hy + bet_min)
      gamYmin[i] = gam_min/(alf_min + bet_min/hy)
      betYmax[i] = bet_max/(alf_max*hy + bet_max)
      gamYmax[i] = gam_max/(alf_max + bet_max/hy)

   for j in range(2,ny):
      (alf_min,bet_min,gam_min,alf_max,bet_max,gam_max) = CondX(y[j])
      betXmin[j] = bet_min/(alf_min*hx + bet_min)
      gamXmin[j] = gam_min/(alf_min + bet_min/hx)
      betXmax[j] = bet_max/(alf_max*hx + bet_max)
      gamXmax[j] = gam_max/(alf_max + bet_max/hx)

   for it in range(1,itmax+1): 
      err = 0e0
      j = 1
      for i in range(1,nx+1):
         uij = betYmin[i]*u[i][2] + gamYmin[i]
         eij = 1e0 - u[i][j]/uij if uij else uij - u[i][j]
         if (fabs(eij) > err): err = fabs(eij)
         u[i][j] = uij

      for j in range(2,ny):
         i = 1
         uij = betXmin[j]*u[i+1][j] + gamXmin[j]
         eij = 1e0 - u[i][j]/uij if uij else uij - u[i][j]
         if (fabs(eij) > err): err = fabs(eij)
         u[i][j] = uij

         for i in range(2,nx):
            uij = (kx*(u[i-1][j] + u[i+1][j]) +
                   ky*(u[i][j-1] + u[i][j+1]) - f[i][j]) / kxy
            eij = 1e0 - u[i][j]/uij if uij else uij - u[i][j] 
            if (fabs(eij) > err): err = fabs(eij)
            u[i][j] = uij

         i = nx
         uij = betXmax[j]*u[i-1][j] + gamXmax[j]
         eij = 1e0 - u[i][j]/uij if uij else uij - u[i][j]
         if (fabs(eij) > err): err = fabs(eij)
         u[i][j] = uij

      j = ny
      for i in range(1,nx+1):
         uij = betYmax[i]*u[i][ny-1] + gamYmax[i]
         eij = 1e0 - u[i][j]/uij if uij else uij - u[i][j]
         if (fabs(eij) > err): err = fabs(eij)
         u[i][j] = uij

      if (err <= eps): break

   if (it >= itmax):
      print("PoissonXY: Se excedió el número máximo de iteraciones !"); return 1
   return 0

#----------------------------------------------------------------------------
def Poisson2D(u, x, y, imin, imax, nx, ny, eps, Func):

   itmax = 10000

   f = [[0]*(ny+1) for i in range(nx+1)]

   hx = (x[nx] - x[1])/(nx-1); kx = 1e0/(hx*hx)
   hy = (y[ny] - y[1])/(ny-1); ky = 1e0/(hy*hy) 
   kxy = 2e0*(kx + ky)

   for j in range(2, ny):
      for i in range(2, nx): f[i][j] = Func(x[i], y[j])

   for it in range(1,itmax+1):
      err = 0e0
      for j in range(2,ny):
         for i in range(imin[j]+1,imax[j]):
            uij = (kx*(u[i-1][j] + u[i+1][j]) - f[i][j]) / kxy
            if (i >= imin[j-1] and i <= imax[j-1]): uij += ky*u[i][j-1] / kxy
            if (i >= imin[j+1] and i <= imax[j+1]): uij += ky*u[i][j+1] / kxy

            eij = 1e0 - u[i][j]/uij if uij else uij - u[i][j]
            if (fabs(eij) > err): err = fabs(eij)
            u[i][j] = uij

      if (err <= eps): break

   if (it >= itmax):
      print("Poisson2D: Se excedió el número máxio de iteraciones !"); return 1
   return 0
