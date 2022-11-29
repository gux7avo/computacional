
import numpy as np
from ModuloPoisson import PoissonXY

def Func(x, y):
   return 

def CondX(y):
   alf_min = 1e0; bet_min = 0e0; gam_min = 0e0
   alf_max = 1e0; bet_max = 0e0; gam_max = 0e0
   return (alf_min, bet_min, gam_min, alf_max, bet_max, gam_max)

def CondY(x):
   alf_min = 1e0; bet_min = 0e0; gam_min = 0e0
   alf_max = 1e0; bet_max = 0e0; gam_max = 0e0
   return (alf_min, bet_min, gam_min, alf_max, bet_max, gam_max)


xmin = -np.pi; xmax = np.pi; ymin = -np.pi; ymax = np.pi
nx = ; ny = 
eps = 

u = [[0]*(ny+1) for i in range(nx+1)]
x = [0]*(nx+1); y = [0]*(ny+1)

hx = (xmax-xmin)/(nx-1)
for i in range(1, nx+1): x[i] = xmin + (i-1)*hx
hy = (ymax-ymin)/(ny-1)
for j in range(1, ny+1): y[j] = ymin + (j-1)*hy

for j in range(1, ny+1):
   for i in range(1, nx+1): u[i][j] = 0e0

PoissonXY(u,x,y,nx,ny,eps,Func,CondX,CondY)

salida = open("Poisson.txt","w")
salida.write("x \t y \t u\n")
for j in range(1, ny+1):
   for i in range(1, nx+1):
      salida.write(("{0:10.5f} \t {1:10.5f} \t {2:14.5e}\n").format(x[i],y[j],u[i][j]))
salida.close()
