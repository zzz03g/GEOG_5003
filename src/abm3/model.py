# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:18:17 2023

@author: ljper
"""
# imports
import random
import math
import matplotlib.pyplot as plt
import operator
import time

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
            distance_calc = get_distance(a[0], a[1], b[0], b[1])
            # print("distance between", a, b, distance_calc)
            max_distance = max(max_distance, distance_calc) # calculate max distance
            # print("max distance", max_distance)
    return max_distance

# create a list to store agents
agents = []
n_agents = 10
for i in range(n_agents):
    agents.append([random.randint(0,99), random.randint(0,99)])
print(agents)

start = time.perf_counter() # record start time
maximum_distance = get_max_distance(agents) # call maximum distance calculation
end = time.perf_counter() # record end time
print("Time take to calculate max distance", end - start, "seconds")
print("Maximum distance between agents at initialisation", maximum_distance)

# Change x and y randomly
for i in range(n_agents):
    # x co-ordinate
    rn = random.random()
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    
    # y co-ordinate
    rn = random.random()
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print(agents)

maximum_distance = get_max_distance(agents) # call maximum distance calculation
print("Maximum distance between agents at end", maximum_distance)

# Get the coordinates with the largest x-coordinate
x_max = max(agents, key=operator.itemgetter(0))
x_min = min(agents, key=operator.itemgetter(0))
y_max = max(agents, key=operator.itemgetter(1))
y_min = min(agents, key=operator.itemgetter(1))
# print(x_max)
# print(x_min)
# print(y_max)
# print(y_min)

#Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
    plt.scatter(agents[i][0], agents[i][1], color='black')
plt.scatter(x_max[0], x_max[1], color='red')
plt.scatter(x_min[0], x_min[1], color='blue')
plt.scatter(y_max[0], y_max[1], color='yellow')
plt.scatter(y_min[0], y_min[1], color='green')
plt.show()

