# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 02:30:08 2022

@author: Lance
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as int

# Weights
# Repulsiveness between of robots
C1 = 1
# Repulsiveness of obstacles
C2 = 3
# Robots
robot1_start = (-1,0)
robot1_end = (0,0)
robot2_start = (-1,4)
robot2_end = (6,0)
robot3_start = (-1,4)
robot3_end = (6,0)
# Obstacles
obs1_radius = 1
obs1_pos = (-2,2)
# Guess
robot1_x = 6
robot1_y = 11
robot2_x = -12
robot2_y = 12
robot3_x = 6
robot3_y = 11





def dxydt(t, x_y):
    x1,y1,x2,y2,x3,y3,x4,y4,dx1,dy1,dx2,dy2,dx3,dy3,dx4,dy4=x_y

    x1_el = -(C1 * (x1 - x2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (x1 - 2) / (np.sqrt((x1 - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1]) ** 2) - obs1_radius) ** 3 / np.sqrt((x1 - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1]) ** 2)

    y1_el = -(C1 * (y1 - y2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (y1 - 2) / (np.sqrt((x1 - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1]) ** 2) - obs1_radius) ** 3 / np.sqrt((x1 - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1]) ** 2)

    x2_el = (C1 * (x1 - x2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (x2 - 2) / (np.sqrt((x2 - obs1_pos[0]) ** 2 + (y2 - obs1_pos[1]) ** 2) - obs1_radius) ** 3 / np.sqrt((x2 - obs1_pos[0]) ** 2 + (y2 - obs1_pos[1]) ** 2)

    y2_el = (C1 * (y1 - y2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (y2 - 2) / (np.sqrt((x2 - obs1_pos[0]) ** 2 + (y2 - obs1_pos[1]) ** 2) - obs1_radius) ** 3 / np.sqrt((x2 - obs1_pos[0]) ** 2 + (y2 - obs1_pos[1]) ** 2)
    
    x_3el = -(C1 * (x3 - x4)) / ((x3 - x4) ** 2 + (y3 - y4) ** 2) ** 2 - C2 * (x3 - 2) / (np.sqrt((x3 - obs1_pos[0]) ** 2 + (y3 - obs1_pos[1]) ** 2) - obs1_radius) ** 3 / np.sqrt((x3 - obs1_pos[0]) ** 2 + (y3 - obs1_pos[1]) ** 2)

    y_3el = -(C1 * (y3 - y4)) / ((x3 - x4) ** 2 + (y3 - y4) ** 2) ** 2 - C2 * (y3 - 2) / (np.sqrt((x3 - obs1_pos[0]) ** 2 + (y3 - obs1_pos[1]) ** 2) - obs1_radius) ** 3 / np.sqrt((x3 - obs1_pos[0]) ** 2 + (y3 - obs1_pos[1]) ** 2)
    
    x_4el = (C1 * (x3 - x4)) / ((x3 - x4) ** 2 + (y3 - y4) ** 2) ** 2 - C2 * (x4 - 2) / (np.sqrt((x3 - obs1_pos[0]) ** 2 + (y4 - obs1_pos[1]) ** 2) - obs1_radius) ** 3 / np.sqrt((x4 - obs1_pos[0]) ** 2 + (y4 - obs1_pos[1]) ** 2) 
    
    y_4el = (C1 * (y3 - y4)) / ((x3 - x4) ** 2 + (y3 - y4) ** 2) ** 2 - C2 * (y4 - 2) / (np.sqrt((x4 - obs1_pos[0]) ** 2 + (y4 - obs1_pos[1]) ** 2) - obs1_radius) ** 3 / np.sqrt((x4 - obs1_pos[0]) ** 2 + (y4 - obs1_pos[1]) ** 2)
    
    return dx1, dy1, dx2, dy2, dx3, dy3 , dx4, dy4, x1_el, y1_el, x2_el, y2_el, x_3el, y_3el, x_4el, y_4el

def bc(ya, yb):
    return ya[0] - robot1_start[0], yb[0] - robot1_end[0] , ya[1] - robot1_start[1], yb[1] - robot1_end[1], ya[2] - robot2_start[0], yb[2] - robot2_end[0], ya[3] - robot2_start[1], yb[3] - robot2_end[1],ya[4] - robot3_start[0], yb[4] - robot3_end[0] , ya[5] - robot3_start[1], yb[5] - robot3_end[1]

t_guess = np.linspace(0, 1, 5)
xy_guess = np.zeros((16, t_guess.size))
xy_guess[0] = robot1_x
xy_guess[1] = robot1_y
xy_guess[2] = robot2_x
xy_guess[3] = robot2_y
xy_guess[4] = robot3_x
xy_guess[5] = robot3_y
res = int.solve_bvp(dxydt, bc, t_guess, xy_guess)


t = np.linspace(0, 1, 201)
obs_t = np.linspace(0, 2 * np.pi, 51)
plt.plot(res.sol(t)[0], res.sol(t)[1], label = 'Robot 1')
plt.plot(res.sol(t)[2], res.sol(t)[3], label = 'Robot 2')
plt.plot(res.sol(t)[4], res.sol(t)[5], label = 'Robot 3')
plt.plot(obs1_radius * np.cos(obs_t) + obs1_pos[0], obs1_radius * np.sin(obs_t),obs1_pos[1], obs1_radius * np.sin(obs_t),obs1_pos[2], obs1_radius * np.sin(obs_t),obs1_pos[3], label = 'obstacle')
plt.legend()


t = np.linspace(0, 1, 101)
plt.plot(t, res.sol(t)[0], label = 'X-Robot 1')
plt.plot(t, res.sol(t)[1], label = 'Y-Robot 2')
plt.plot(t, res.sol(t)[2], label = 'X-Robot 1')
plt.plot(t, res.sol(t)[3], label = 'Y-Robot 2')
plt.legend()

