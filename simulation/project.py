import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# weights

C1 = 1 
C2 = 1 

# user input for testing

# boundary conditions for first robot
robot1i = input("Enter starting coordinate of first robot: ")
robot1f = input("Enter ending coordinate of first robot:  ")

robot1_start = tuple([int(item) for item in robot1i.split(',')])
robot1_end = tuple([int(item) for item in robot1f.split(',')])

# boundary conditions for second robot
robot2i = input("Enter starting coordinate of second robot: ")
robot2f = input("Enter ending coordinate of second robot:  ")

robot2_start = tuple([int(item) for item in robot2i.split(',')])
robot2_end = tuple([int(item) for item in robot2f.split(',')])


# Boundary Conditions

# robot1_start = (1,0)
# robot1_end = (2,1)
# robot2_start = (0,0)
# robot2_end = (1,5)

# Guess

robot1_x = 0 
robot1_y = 9
robot2_x = 5
robot2_y = 6

def dxydt (t, x_y):
    x1, y1, x2, y2, dx1, dy1, dx2, dy2 = x_y
    try:
        x1_el = -(C1 * (x1 - x2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) - C2 * (x1 - 2) / (np.sqrt((x1 - 2) ** 2  + (y1 - 2) ** 2) -2) ** 3 / np.sqrt((x1 - 2) ** 2 + (y1 - 2) ** 2) 
        y1_el = -(C1 * (y1 - y2)) / ((x1  - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (y1 - 2) / (np.sqrt((x1 - 2) + (y1 - 2) ** 2) - 2) ** 3 / np.sqrt((x1  - 2) ** 2 + (y1 - 2) ** 2)   
        x2_el = (C1 *  (x1 - x2)) / ((x1  - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (x2 - 2) / (np.sqrt(x2 - 2 ** 2 + (y2 - 2) ** 2) -2 ) ** 3 / np.sqrt((x2  - 2) ** 2 + (y2 - 2) ** 2) 
        y2_el = (C1 * (y1 - y2)) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2 - C2 * (y2 - 2) / (np.sqrt((x2 - 2) ** 2 + (y2 - 2) ** 2) - 2) **3 / np.sqrt((x2 - 2 ) ** 2 + (y2 - 2) ** 2)

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

plt.plot(np.cos(obs_t) + 5, np.sin(obs_t) + 5, label = 'obstacle')
plt.legend()

plt.show()
