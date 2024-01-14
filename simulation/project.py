import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as int

# weights

C1 = 1 
C2 = 1 

# Boundary Conditions

robot1_start = (-5,0)
robot1_end = (5,5)
robot2_start = (5,0)
robot2_end = (-5,-5)

# Guess

robot1_x = 0 
robot1_y = 9
robot2_x = 5
robot2_y = 6

def dxydt (t, x_y):
    x1, y1, x2, y2, dx1, dy1, dx2, dy2 = x_y

    x1_el = - (C1 * (x1 - x2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (x1 - 2) / (np.sqrt((x1 -2) ** 2 + (y1 - 2) ** 2) - 2 ) ** 3 / np.sqrt((x1 - 2) ** 2 + (y1 - 2 ) ** 2 )

    y1_el =  - (C1 * (y1 - y2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (y1 - 2) / ((np.sqrt(x1 - 2) ** 2 + (y1 - 2) ** 2) - 2) ** 3  / np.sqrt((x1 - 2) ** 2 + (y1 - 2) ** 2) 

    x2_el = (C1 * (x1 - x2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (x2 - 2) / (np.sqrt((x2 - 2) ** 2 + (y2 - 2) ** 2) - 2 ) ** 3 / np.sqrt((x2 - 2) ** 2 + (y2 - 2) ** 2) 

    y2_el  = (C1 * (y1 - y2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2)  ** 2 - C2 * (y2 -2) / (np.sqrt( (x2 - 2 ) ** 2 + (y2 - 2) ** 2  ) - 2) ** 3 / np.sqrt((x2 - 2) + (y2 -2) ** 2)
    return dx1 , dy1 , dx2 , dy2 , x1_el, y1_el , x2_el, y2_el

def boundCond (ya, yb):
    return ya[0] - robot1_start[0], yb[0] - robot1_end[0], ya[1] - robot1_start[1], yb[1] - robot1_end[1], ya[2] - robot2_start[0], yb[2] - robot2_end[0], ya[3] - robot2_start[1], yb[3] - robot2_end[1]

t_guess = np.linspace(0,1,5)
xy_guess = np.zeros((8, t_guess.size))

xy_guess[0] = robot1_x
xy_guess[1] = robot1_y
xy_guess[2] = robot2_x
xy_guess[3] = robot2_y

res = int.solve_bvp(dxydt, boundCond, t_guess, xy_guess)

# Paths of Robots

t = np.linspace(0,1,101)
obs_t = np.linspace(0,2 * np.pi, 50)

plt.plot(res.sol(t)[0], res.sol(t)[1], label = 'Robot 1')
plt.plot(res.sol(t)[2], res.sol(t)[3], label = 'Robot 2')

plt.plot(2 * np.cos(obs_t) + 2, 2 * np.sin(obs_t) + 2, label = 'obstacle')
plt.legend()

plt.show()
