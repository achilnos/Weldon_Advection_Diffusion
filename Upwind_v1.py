import numpy as np
import math

GRIDS = []

#w is the width of the cosine;n is resolution;f is the initial condition
def grid_init(n,w,f):
    return np.array([f(1.0*x*w/n+w/(2.0*n)) for x in range(0, n)])
    
#print grid_init(100,1,lambda x: math.cos(2*math.pi*x))

def space_loop(m, h, hh):
    i = 0
    grid = np.zeros(m)#having this vector be bigger than m allow convient boundary condition calculations
    while(i < m):
        x = i * h - hh
        f = lambda x: math.cos(2*math.pi*x)
        grid[i] = f(x)
        i = i + 1
    print grid
    GRIDS.append(grid)
    oldgrid = grid
    #time_loop(oldgrid, h, m)
    
def grid_maker(initsize, n):
    i = 0
    m = initsize
    while(i < n):
        i = i + 1
        h = 1.0 / m
        hh = h / 2.0
        space_loop(m, h, hh)
        m = 2 * m


grid_maker(3,4)
