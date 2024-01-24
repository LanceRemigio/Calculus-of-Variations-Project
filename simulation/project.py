import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Repulsiveness between robots

C1 = 1 

# Replusiveness of obstacles

C2 = 3

# user input for testing

# boundary conditions for first robot
robot1i = input("Enter starting coordinate of first robot: ")
robot1f = input("Enter ending coordinate of first robot:  ")

robot1_start = tuple(
        [int(item) for item in robot1i.split(',')]
        )
robot1_end = tuple(
        [int(item) for item in robot1f.split(',')]
        )

# boundary conditions for second robot
robot2i = input("Enter starting coordinate of second robot: ")
robot2f = input("Enter ending coordinate of second robot:  ")

robot2_start = tuple(
        [int(item) for item in robot2i.split(',')]
        )

robot2_end = tuple(
        [int(item) for item in robot2f.split(',')]
        )

obs1_posIn = input("Enter coordinate of obstacle: ")
obs1_pos = tuple(
        [int(item) for item in obs1_posIn.split(',')]
        )

obs1_radius = int(input("Enter the radius of obstacle: "))

# Guess

robot1_x = 2 
robot1_y = 3
robot2_x = 6
robot2_y = 4

def dxydt (t, x_y):
    x1, y1, x2, y2, dx1, dy1, dx2, dy2 = x_y
    try:
        x1_el = -(C1 * (x1 - x2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) - C2 * (x1 - 2) / (np.sqrt((x1 - obs1_pos[0]) ** 2  + (y1 - obs1_pos[1]) ** 2) -obs1_radius) ** 3 / np.sqrt((x1 - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1]) ** 2)

        y1_el = -(C1 * (y1 - y2)) / ((x1  - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (y1 - 2) / (np.sqrt((x1 - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1]) ** 2) - obs1_radius) ** 3 / np.sqrt((x1  - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1]) ** 2)   

        x2_el = (C1 *  (x1 - x2)) / ((x1  - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (x2 - 2) / (np.sqrt( (x2 - obs1_pos[0]) ** 2 + (y2 - obs1_pos[1]) ** 2) - obs1_radius ) ** 3 / np.sqrt((x2  - obs1_pos[0]) ** 2 + (y2 - obs1_pos[1]) ** 2) 

        y2_el = (C1 * (y1 - y2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (y2 - 2) / (np.sqrt((x2 - obs1_pos[0]) ** 2 + (y2 - obs1_pos[1]) ** 2) - obs1_radius ) **3 / np.sqrt((x2 - obs1_pos[0] ) ** 2 + (y2 - obs1_pos[1]) ** 2)

        return dx1, dy1, dx2, dy2, x1_el, y1_el, y2_el, x2_el,
    except:
        return 0

def boundCond (ya, yb):
    return ya[0] - robot1_start[0], yb[0] - robot1_end[0], ya[1] - robot1_start[1], yb[1] - robot1_end[1], ya[2] - robot2_start[0], yb[2] - robot2_end[0], ya[3] - robot2_start[1], yb[3] - robot2_end[1]

t_guess = np.linspace(0,1,5)
xy_guess = np.zeros((8, t_guess.size))

xy_guess[0] = robot1_x
xy_guess[1] = robot1_y
xy_guess[2] = robot2_x
xy_guess[3] = robot2_y

res = integrate.solve_bvp(dxydt, boundCond, t_guess, xy_guess)

# Paths of Robots

t = np.linspace(0,1,101)
obs_t = np.linspace(0, 2 * np.pi, 100)

plt.plot(res.sol(t)[0], res.sol(t)[1], label = 'Robot 1')
plt.plot(res.sol(t)[2], res.sol(t)[3], label = 'Robot 2')

plt.plot(obs1_radius * np.cos(obs_t) + obs1_pos[0], obs1_radius * np.sin(obs_t) + obs1_pos[1], label = 'obstacle')
plt.legend()

plt.show()
