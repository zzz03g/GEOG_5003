# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:18:17 2023

@author: ljper
"""
# imports
# import random
import math
import matplotlib.pyplot as plt
import operator
import time

import my_modules.agentframework as af
import my_modules.io as io

# Set the pseudo-random seed for reproducibility
'''random.seed(0)'''

def get_distance(x0, y0, x1, y1):
    """
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).
    
    Keyword arguments:
    x0 -- an integer (no default)
    x1 -- an integer (no default)
    y0 -- an integer (no default)
    y1 -- an integer (no default)
    
    Returns:
    The Euclidean distance between (x0, y0) and (x1, y1)
    """
    xdiff = x0 - x1
    ydiff = y0 - y1
    xydist = math.sqrt(xdiff**2 + ydiff**2)
    return xydist

def get_max_distance(input_coords):
    """
    Calulate the maximum distance between agents
    
    Keyword arguments:
    input_coords -- a list of co-ordinates

    Returns:
    The maximum Euclidean distance between co-ordinates

    """
    max_distance = 0 # initialise max_distance
    for a in input_coords:
        for b in input_coords: 
            distance_calc = get_distance(a.x, a.y, b.x, b.y)
            # print("distance between", a, b, distance_calc)
            max_distance = max(max_distance, distance_calc) # calculate max distance
            # print("max distance", max_distance)
    return max_distance

def sum_environment(environment, n_rows, n_cols):
    '''
    Sum the total resource remaining in the environment
    
    Arguments
    ---------
    environment - a list
        A list of the remaining resource at each location in the environment
    n_rows - integer
        The number of rows in the environment
    n_cols - integer
        The number of columns in the environment

    Returns
    -------
    total_environment - float
        The sum of the remaining resource in the environment

    '''
    total_environment = 0
    for x in range(n_cols): # loop through columns
        for y in range(n_rows): # loop through rows
            total_environment += environment[x][y] # sum environment
            
    return total_environment

def sum_stores(n_agents):
    '''
    Sum the stores of all the agents
    
    Arguments
    ---------
    n_agents - integer
        The number of agents

    Returns
    -------
    total_stores - float
        The sum of the resource stored by the agents
    

    '''
    total_stores = 0
    for n in range(n_agents):
        total_stores += agents[n].store
        
    return total_stores

# Open the environment data
error, n_rows, n_cols, environment = io.read_data()

#n_agents = input("Key in a positive integer between 10 and 100 to set the"
#+ " number of agents then press the <ENTER> or <RETURN> key:")
#print("The input detected is:", n_agents)
# create a list to store agents
n_agents = 10
n_iterations = 100

# Variables for constraining movement
x_min = 0 # minimum x coordinate
y_min = 0 # minimum y coordinate
x_max = n_cols - 1 # maximum x coordinate
y_max = n_rows - 1 # maximum y coordinate

# Initialise agents
agents = []
#a = af.Agent()
#print("type(a)", type(a))
#print("a", a)
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(i, environment, n_rows, n_cols))
    print(agents[i])
print(agents)

# Calculate the total resource and stores at the start
total_resource = sum_environment(environment,n_rows,n_cols)
total_stores = sum_stores(n_agents)
total_at_start = total_resource + total_stores

start = time.perf_counter() # record start time
maximum_distance = get_max_distance(agents) # call maximum distance calculation
end = time.perf_counter() # record end time
print("Time take to calculate max distance", end - start, "seconds")
print("Maximum distance between agents at initialisation", maximum_distance)

# Change x and y randomly
for j in range(n_iterations):
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max) # move the agent
        agents[i].eat() # allow the agent to eat (NB agents processed first get priority to depleting resources)

maximum_distance = get_max_distance(agents) # call maximum distance calculation
print("Maximum distance between agents at end", maximum_distance)


# Calculate the total resource and stores at the end
total_resource = sum_environment(environment,n_rows,n_cols)
total_stores = sum_stores(n_agents)
total_at_end = total_resource + total_stores

# Check nothing has gone missing
if total_at_start == total_at_end:
    print("Hoorah")
else:
    print("Something has gone missing")
    
# Write the final environment to a file
io.write_to_file(environment)

# Get the coordinates with the largest x-coordinate
lx = max(agents, key=operator.attrgetter('x'))
sx = min(agents, key=operator.attrgetter('x'))
ly = max(agents, key=operator.attrgetter('y'))
sy = min(agents, key=operator.attrgetter('y'))
# print(x_max)
# print(x_min)
# print(y_max)
# print(y_min)


#Plot the agents
plt.imshow(environment)
for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
    plt.scatter(agents[i].x, agents[i].y, color='black')
plt.scatter(lx.x, lx.y, color='red')
plt.scatter(sx.x, sx.y, color='blue')
plt.scatter(ly.x, ly.y, color='yellow')
plt.scatter(sy.x, sy.y, color='green')

#plt.ylim(y_min, y_max)
#plt.xlim(x_min, x_max)
plt.ylim(y_max / 3, y_max * 2/3)
plt.xlim(x_min / 3, x_max * 2/3)
plt.show()

