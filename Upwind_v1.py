import numpy as np
import math

GRIDS = []

#w is the width of the cosine;n is resolution;f is the initial condition
def grid_init(n,w,f):
    return np.array([f(1.0*x*w/n+w/(2.0*n)) for x in range(0, n)])
    
#print grid_init(100,1,lambda x: math.cos(2*math.pi*x))

def time_loop(h, hh, m, timemax, a, sigma):
    print "time loop m = " + str(m)
    t = 0
    dt = sigma * h / a
    nmax = timemax / dt
    print "nmax =", nmax
    print "dt =", dt
    if nmax * dt < timemax:
        nmax = nmax + 1
    while(t < nmax):
        if t + dt > timemax:
            dt = timemax - t
        space_loop(m, h, hh)
        t = t + dt
    print "t =", t
        #actual upwind calculation next line

def space_loop(m, h, hh):
    print "space loop m = " + str(m)
    i = 0
    grid = np.zeros(m)#having this vector be bigger than m allow convient boundary condition calculations
    while(i < m):
        x = i * h - hh
        f = lambda x: math.cos(2*math.pi*x)
        grid[i] = f(x) #index out of bounds error!
        i = i + 1
    print grid
    GRIDS.append(grid)
    oldgrid = grid
    
def grid_maker(initsize, n, timemax, a, sigma):
    i = 0
    m = initsize
    print "grid_make m = " + str(m)
    while(i < n):
        i = i + 1
        h = 1.0 / m
        hh = h / 2.0
        time_loop(m, h, hh, timemax, a, sigma)
        #space_loop(m, h, hh)
        m = 2 * m

def define_variables():    
    initsize = input("enter number of cells in grid: ")
    n = input("enter length of grid: ")
    timemax = input("enter number of timesteps: ")
    a = input("enter a value for a: ")
    sigma = input("enter a value for sigma: ")
    grid_maker(initsize, n, timemax, a, sigma)

define_variables()
