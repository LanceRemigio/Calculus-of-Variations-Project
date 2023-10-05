import numpy as np
import matplotlib.pyplot as plt
import diffeq as df
import scipy.integrate as int


# Weights
# Repulsiveness between of robots 

c_1 = 1 

# Repulsivness of obstacles

c_2 = 3


# Robots
robot1_start = (1,2) #insert initial position for robot 1
robot1_end = (3,1) #insert final position for robot 1
robot2_start = (0,1)#insert initial position for robot 2
robot2_end = (5,1)#insert final position for robot 2
##
## Obstacles
obs1_radius = 4 #specify size of radius of obstacle
obs1_pos = (0,0) #specify location of center of obstacle
##
robot1_x =  0  #insert guess for x position for robot 1
robot1_y = 0  #insert guess for y position for robot 1
robot2_x = 0 #insert guess for x position for robot 2
robot2_y = 0 #insert guess for y position for robot 2

t_guess = np.linspace(0,1,5) 

xy_guess = np.zeros((8, t_guess.size))

xy_guess[0] = robot1_x
xy_guess[1] = robot1_y
xy_guess[2] = robot2_x
xy_guess[3] = robot2_y


def boundary_conditions (ya, yb):
    boundaryCond = [ 
                    ya[0] - robot1_start[0], yb[0] - robot1_end[0], 
                    ya[1] - robot1_start[1], yb[1] - robot1_end[1],
                    ya[2] - robot2_start[0], yb[2] - robot2_end[0],
                    ya[3] - robot2_start[1], yb[3] - robot2_end[1] 
                    ]
    return  boundaryCond[0], boundaryCond[1], boundaryCond[2], boundaryCond[3]



res = int.solve_bvp(df.diff_func
                    ,boundary_conditions,
                    t_guess, xy_guess)

