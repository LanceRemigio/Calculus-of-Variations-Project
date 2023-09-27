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


# -(c1 * (x1 - x2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2 )
# - c2 * (x1 - 2) / (np.sqrt((x1 - obs1_pos[0])) ** 2 
#  (y1 - obs1_pos[1]) **2) - obs1_radius) ** 3 / np.sqrt((x1 - obs_pos[0]) ** 2 + (y1 - obs1_pos[1]) ** 2)

# 

# This function is doing too much 
# Original function is unreadable 

def x1_el (x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius):
    delt_x = x1 - x2
    delt_y = y1 - y2
    list_terms = [ 
                    (c1 * delt_x) / sum((delt_x) ** 2, (delt_y) ** 2 ) ** 2,      

                    (c2 *  (x1 - 2)) / (np.sqrt(x1 - obs1_pos[0])) ** 2, 

                    (y1 - obs1_pos[1] ** 2 - obs1_radius) ** 3 
                    / np.sqrt((x1 - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1] ** 2 ))
                ]
    return -list_terms[0] - list_terms[1] + list_terms[2]     

def y1_el (x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius):
    delt_x = x1 - x2
    delt_y = y1 - y2
    list_terms = [ 
                    (c1 * delt_y) / sum((delt_x) ** 2, (delt_y) ** 2 ) ** 2,      

                    (c2 *  (y1 - 2)) / (np.sqrt(x1 - obs1_pos[0])) ** 2, 

                    (y1 - obs1_pos[1] ** 2 - obs1_radius) ** 3 
                    / np.sqrt((x1 - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1] ** 2 ))
                ]
    return -list_terms[0] - list_terms[1] + list_terms[2]


def x2_el (x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius):
    return 0

def y2_el (x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius):
    return 0


def diff_func (x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius):
    list_func = [ x1_el(x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius), 
                    y1_el(x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius),   
                ] 
    return list_func
def boundary_conditions (ya, yb):
    return ya[0] - robot1_start[0], yb[0] - robot1_end[0], ya[1] - robot1_start[1], yb[1] - robot1_end[1], ya[2] - robot2_start[0], yb[2] - robot2_end[0], ya[3] - robot2_start[1], yb[3] - robot2_end[1]

t_guess = np.linspace(0,1,5) 

xy_guess = np.zeros((8, t_guess.size))

xy_guess[0] = robot1_x
xy_guess[1] = robot1_y
xy_guess[2] = robot2_x
xy_guess[3] = robot2_y

res = int.solve_bvp(diff_func, boundary_conditions, t_guess, xy_guess)

