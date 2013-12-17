Weldon_Advection_Diffusion
==========================

As a learning exercise, Nicholas is writing programs in python that use numerical discretization methods to approximate the solutions to advection and diffusion problems. 

The first of these programs is a script designed to use the upwind scheme, which is first order finite difference method, to approximate the solution to the 1D advection equation du/dt + a*du/dx = 0. 

Structure: The script is written in python, importing the numpy and math modules. define_variables() defines the variables according to input given through the terminal depending on the desired number of cells in the grid, the length of the grid, the number of timesteps, the value of sigma in the upwind scheme, and the value of a in the advection equation. These variables are passed to grid_maker

Current Status: The script has been shown to run correctly within each function. However, connecting the functions causes a bug where the value of variabel "m" is changed by a seemingly random amount when it is passed through the function "time_loop()." The new value of m is always less than one, which causes the "index out of bounds" error at line 36. I will continue to work on fixing this, also exporting the data generated to matlab, and adding a snippet to measure convergence. 

