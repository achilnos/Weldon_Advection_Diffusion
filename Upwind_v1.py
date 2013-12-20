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

def result(newgrid):
    print "the state of the system at the final timestep is: ", newgrid

def time_loop(initsize, h, hh, timemax, a, sigma):
    t = 0
    dt = sigma * h / a
    nmax = timemax / dt
    oldgrid = np.zeros(initsize)#having this vector be bigger than m allow convient boundary condition calculations
    newgrid = np.zeros(initsize)
    set_initial(initsize, h, hh, sigma, dt, oldgrid, newgrid)
    if nmax * dt < timemax:
        nmax = nmax + 1
    while(t < nmax):
        if t + dt > timemax:
            dt = timemax - t
            if dt == 0:
                result(oldgrid)
                break
        space_loop(initsize, h, hh, sigma, dt, oldgrid, newgrid)
        oldgrid = newgrid
        print "oldgrid = ", oldgrid
        print "newgrid = ", newgrid
        t = t + dt

def set_initial(initsize, h, hh, sigma, dt, oldgrid, newgrid):
    #print "space loop initsize = " + str(initsize)
    i = 0
    while(i < initsize):
        x = i * h - hh
        f = lambda x: math.cos(2*math.pi*x)
        oldgrid[i] = f(x)
        i = i + 1
    
def space_loop(initsize, h, hh, sigma, dt, oldgrid, newgrid):#actual upwind method calculation
    GRIDS.append(oldgrid)
    j = 0
    while(j < len(oldgrid) - 1):
        j = j + 1
#    for j in oldgrid[1:len(oldgrid)-1]:#the range set up wrong, causing no count
#        #this is where the problem is: j is not counting!
        print "newgrid", j, " = ", newgrid[j]
        print "oldgrid", j, " = ", oldgrid[j]
        newgrid[j] = oldgrid[j] + sigma * dt * (oldgrid[j-1] - oldgrid[j])#this is just adding zeros!
    newgrid[0] = oldgrid[0] + sigma * dt * (oldgrid[len(oldgrid)-1] - oldgrid[0])#this works
    print newgrid#this result is not evolving!
    
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
