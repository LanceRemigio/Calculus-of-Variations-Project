import numpy as np
import matplotlib.pyplot as plt
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


