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

# Set the pseudo-random seed for reproducibility
'''random.seed(0)'''

# create a list to store agents
agents = []
n_agents = 20
for i in range(n_agents):
    agents.append([random.randint(0,99), random.randint(0,99)])
print(agents)

# Change x and y randomly
for i in range(n_agents):
    # x co-ordinate
    rn = random.random()
    print("rn", rn)
    
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    
    # y co-ordinate
    rn = random.random()
    print("rn", rn)
    
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print(agents)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
xdiff = agents[0][0] - agents[1][0]
ydiff = agents[0][1] - agents[1][1]
xydist = math.sqrt(xdiff**2 + ydiff**2)
print("xydist", xydist)

# Get the coordinates with the largest x-coordinate
x_max = max(agents, key=operator.itemgetter(0))
x_min = min(agents, key=operator.itemgetter(0))
y_max = max(agents, key=operator.itemgetter(1))
y_min = min(agents, key=operator.itemgetter(1))
print(x_max)
print(x_min)
print(y_max)
print(y_min)

#Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
    plt.scatter(agents[i][0], agents[i][1], color='black')
plt.scatter(x_max[0], x_max[1], color='red')
plt.scatter(x_min[0], x_min[1], color='blue')
plt.scatter(y_max[0], y_max[1], color='yellow')
plt.scatter(y_min[0], y_min[1], color='green')
plt.show()

