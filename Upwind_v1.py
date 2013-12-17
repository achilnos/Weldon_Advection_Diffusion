import numpy as np
import math

GRIDS = []

#cd ~/Documents/Python/Weldon_Advection_Diffusion

#w is the width of the cosine;n is resolution;f is the initial condition
def grid_init(n,w,f):
    return np.array([f(1.0*x*w/n+w/(2.0*n)) for x in range(0, n)])
    
#print grid_init(100,1,lambda x: math.cos(2*math.pi*x))

def time_loop(initsize, h, hh, timemax, a, sigma):
    t = 0
    dt = sigma * h / a
    print "time_loop dt = ", dt
    print "time_loop h = ", h
    print "time_loop a = ", a
    print "time_loop sigma = ", sigma
    nmax = timemax / dt
    #print "nmax =", nmax
    #print "dt =", dt
    if nmax * dt < timemax:
        nmax = nmax + 1
    while(t < nmax):#this loop continues indefinitly
        if t + dt > timemax:
            dt = timemax - t
            if dt == 0:
                break#this could be the place to call the data comparison function
        space_loop(initsize, h, hh)
        print "innerloop dt = ", dt
        t = t + dt#the problem is dt = 0 here
        #print "t = ", t
    #print "t =", t
        #actual upwind calculation next line

def space_loop(initsize, h, hh):
    print "space loop initsize = " + str(initsize)
    grid = np.zeros(initsize)#having this vector be bigger than m allow convient boundary condition calculations
    i = 0
    while(i < initsize):#this loop exits correctly!
        x = i * h - hh
        f = lambda x: math.cos(2*math.pi*x)
        grid[i] = f(x)
        i = i + 1
    print grid
    GRIDS.append(grid)
    oldgrid = grid
    
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
