# Calculus of Variations Project

A program that simulates paths of robots using principles from Calculus of Variations with a goal of minimizing collisions between obstacles.

# Modules Used

- Matplotlib
- NumPy
- SciPy
- Pandas

# Running the program

First, use git to clone the project into a directory of your choice and cd into the project.

````bash
git clone https://github.com/LanceRemigio/Calculus-of-Variations-Project
cd Calculus-of-Variations-Project
````

To run the program, cd into the `simulation` directory and run the file:

````bash
cd simulation
python3 project.py
````

The program will then prompt you to enter the paths of each robot (via the starting and ending point of their paths) and the location of the obstacle. Make sure to list each coordinate with a comma (with no spaces). For example, running the file will create the following plots:

# Documentation

To get a more in depth look into how the code was derived from the principles used in Calculus of Variations, navigate to the `content` directory and use your pdf-viewer of choice to view the pdf. For example,
````bash
cd content 
zathura main.pdf
````

# TO DO:

- [] Need to refactor the messy code so that it is more readable.
- [] Add more functionality to the simulations



