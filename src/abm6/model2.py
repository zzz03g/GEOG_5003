# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:18:17 2023

@author: ljper
"""
# imports
# import random
import matplotlib.pyplot as plt
import operator
import time
import imageio
import os

import my_modules.agentframework as af
import my_modules.io as io
import my_modules.geometry as geometry

# Set the pseudo-random seed for reproducibility
'''random.seed(0)'''

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
            distance_calc = geometry.get_distance(a.x, a.y, b.x, b.y)
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

if __name__ == '__main__':
    
    # Open the environment data
    error, n_rows, n_cols, environment = io.read_data()
    
    #n_agents = input("Key in a positive integer between 10 and 100 to set the"
    #+ " number of agents then press the <ENTER> or <RETURN> key:")
    #print("The input detected is:", n_agents)
    # create a list to store agents
    n_agents = 10
    n_iterations = 100
    neighbourhood = 20
    
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
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols))
    #    print(agents[i])
    
    # Calculate the total resource and stores at the start
    total_resource = sum_environment(environment,n_rows,n_cols)
    total_stores = sum_stores(n_agents)
    total_at_start = total_resource + total_stores
    
    start = time.perf_counter() # record start time
    maximum_distance = get_max_distance(agents) # call maximum distance calculation
    end = time.perf_counter() # record end time
    print("Time take to calculate max distance", end - start, "seconds")
    print("Maximum distance between agents at initialisation", maximum_distance)
    
    # Create directory to write images to
    try:
        os.makedirs('../../data/output/images')
    except FileExistsError:
        print("Path exists")
        
    # For storing global images
    global ite
    ite = 0
    images = []
    
    # Model loop
    for ite in range(n_iterations):
        print("Iteration", ite)
        
        # Move agents
        print("Move")
        for i in range(n_agents):
            agents[i].move(x_min, y_min, x_max, y_max) # move the agent
            agents[i].eat() # allow the agent to eat (NB agents processed first get priority to depleting resources)
            
        # Share store
        # Distribute shares
        for i in range(n_agents):
            agents[i].share(neighbourhood)
        # Add store shares to store and set store_shares back to zero
        for i in range(n_agents):
            #print(agents[i])
            agents[i].store = agents[i].store_shares
            agents[i].store_shares = 0
        #print(agents)
    
        # Print the maximum distance between agents
        print("Maximum distance between all agents", get_max_distance(agents))
        # Print the total amount of resource
        sum_e = sum_environment(environment,n_rows,n_cols)
        print("Sum environment", sum_e)
        sum_as = sum_stores(n_agents)
        print("Sum agent stores", sum_as)
        print("Total resource", sum_e + sum_as)
    
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
        plt.ylim(y_min, y_max)
        plt.xlim(x_min, x_max)
        filename = '../../data/output/images/image' + str(ite) + '.png'
        plt.savefig(filename)
        plt.show()
        plt.close()
        images.append(imageio.imread(filename))
        
    # Create a GIF from the images
    imageio.mimsave('../../data/output/out.gif', images, fps=3) # 3 frames per second

    # Write the final environment to a file
    io.write_to_file(environment)
