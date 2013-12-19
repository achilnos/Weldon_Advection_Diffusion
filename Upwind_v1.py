import numpy as np
import math

GRIDS = []

#for terminal:
#cd ~/Documents/Python/Weldon_Advection_Diffusion
#python Upwind_v1.py

#more efficent version of grid maker:w is the width of the cosine;n is resolution;f is the initial condition
def grid_init(n,w,f):
    return np.array([f(1.0*x*w/n+w/(2.0*n)) for x in range(0, n)])
    
#print grid_init(100,1,lambda x: math.cos(2*math.pi*x))

def time_loop(initsize, h, hh, timemax, a, sigma):
    t = 0
    dt = sigma * h / a
    nmax = timemax / dt
    if nmax * dt < timemax:
        nmax = nmax + 1
    while(t < nmax):
        if t + dt > timemax:
            dt = timemax - t
            if dt == 0:
                break
        space_loop(initsize, h, hh, sigma, dt)
        print "innerloop dt = ", dt
        t = t + dt

def space_loop(initsize, h, hh, sigma, dt):
    print "space loop initsize = " + str(initsize)
    grid = np.zeros(initsize)#having this vector be bigger than m allow convient boundary condition calculations
    i = 0
    while(i < initsize):
        x = i * h - hh
        f = lambda x: math.cos(2*math.pi*x)
        grid[i] = f(x)
        i = i + 1
    print grid
    GRIDS.append(grid)
    oldgrid = grid
    newgrid = []
    j = 0
    while(j < len(oldgrid) + 1):
        if j == len(oldgrid):
            print "j = ", j
            gridlength = j
            if type(j) == int:
                print "type(j) is an integer"
        j = j + 1
    k = 0
    for k in oldgrid[1:gridlength]:#actual upwind method calculation
        newgrid[k] = oldgrid[k] + sigma * dt * (oldgrid[k-1] - oldgrid[k])#TypeError: list indices must be integers, not numpy.float64--try replacing the for with a while?
    newgrid[0] = oldgrid[0] + sigma * dt * (oldgrid[len(oldgrid)] - oldgrid[0])
    print newgrid
    
def grid_maker(initsize, n, timemax, a, sigma):
    i = 0
    print "grid_make initsize = " + str(initsize)
    while(i < n):
        i = i + 1
        h = 1.0 / initsize
        hh = h / 2.0
        time_loop(initsize, h, hh, timemax, a, sigma)
        initsize = 2 * initsize

def define_variables():    
    initsize = input("enter number of cells in grid: ")
    n = input("enter length of grid: ")
    timemax = input("enter number of timesteps: ")
    a = input("enter a value for a: ")
    sigma = input("enter a value for sigma: ")
    grid_maker(initsize, n, timemax, a, sigma)

define_variables()
