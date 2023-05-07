# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:01:28 2023

@author: Andy Turner
"""
import random
from matplotlib import pyplot as plt
import time
import math

# Set the pseudo-random seed for reproducibility
#random.seed(0)

# A variable to store the number of agents
#n_agents = 500

def get_distance(x0, y0, x1, y1):
    """
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).

    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair.
    y0 : Number
        The y-coordinate of the first coordinate pair.
    x1 : Number
        The x-coordinate of the second coordinate pair.
    y1 : Number
        The y-coordinate of the second coordinate pair.

    Returns
    -------
    distance : Number
        The Euclidean distance between (x0, y0) and (x1, y1).
    """
    # Calculate the difference in the x coordinates.
    dx = x0 - x1
    # Calculate the difference in the y coordinates.
    dy = y0 - y1
    # Square the differences and add the squares
    ssd = (dx * dx) + (dy * dy)
    # Calculate the square root
    distance = ssd ** 0.5
    return distance

def get_min_max_distance():
    """
    Calculate and return the maximum distance between all the agents

    Returns
    -------
    max_distance : Number
        The maximum distance betwee all the agents.

    """
    # Loop through and calculate distances
    max_distance = 0
    min_distance = math.inf
    distance_list = []
    sum_distance = 0
    distance_count = 0

    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            #print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            distance_list.append(distance)
            sum_distance += distance
            distance_count += 1
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            min_distance = min(min_distance, distance)
            #print("max_distance", max_distance)
            distances = [min_distance, max_distance]
    print(distance_list)
    test_max = max(distance_list)
    test_min = min(distance_list)
    test_mean = sum(distance_list) / len(distance_list)
    test_mean2 = sum_distance / distance_count
    print("Test max =", test_max)
    print("Test min =", test_min)
    print("Test mean =", test_mean)
    print("Test mean2 =", test_mean2)
    return distances

# A list to store times
run_times = []
#n_agents_range = range(500, 5000, 500)
n_agents_range = [10]

for n_agents in n_agents_range:
    
    # Initialise agents
    agents = []
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
    #print(agents)
    
    # Print the minimum and maximum distance between all the agents
    start = time.perf_counter()
    [min_dist, max_dist] = get_min_max_distance()
    print("Minimum and Maximum distance between all the agents", min_dist, max_dist)

    end = time.perf_counter()
    run_time = end - start
    print("Time taken to calculate minimum and maximum distances", run_time)
    run_times.append(run_time)

# Plot
plt.title("Time taken to calculate maximum distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Time")
j = 0
for i in n_agents_range:
    plt.scatter(i, run_times[j], color='black')
    j = j + 1
plt.show()
