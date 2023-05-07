# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:18:17 2023

@author: ljper
"""
# imports
#import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import operator
#import time
import imageio
import os
import tkinter as tk

import my_modules.agentframework as af
import my_modules.io as io
import my_modules.geometry as geometry

# Set the pseudo-random seed for reproducibility
'''random.seed(0)'''

def run(canvas):
    '''
    Run the model and generate the animation

    Parameters
    ----------
    canvas : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    animation = anim.FuncAnimation(fig, update, init_func = plot, frames = gen_function, repeat = False)
    animation.new_frame_seq()
    canvas.draw()    

def output():
    '''
    Write the final environment to a file

    Returns
    -------
    None.

    '''
    # Write data
    print ("Write data")
    io.write_to_file('../../data/output/out8.txt', environment)
    # Create a GIF from the images
    imageio.mimsave('../../data/output/out8.gif', images, fps=3) # 3 frames per second
    
def exiting():
    '''
    Exits the program

    Returns
    -------
    None.

    '''
    # Exit the program
    root.quit()
    root.destroy()
    #sys.exit(0)

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

def plot():
    '''
    Plot the agent locations
    
    Parameters
    ----------
    NONE

    Returns
    -------
    fig : FIGURE
        Figure showing agent locations.

    '''
    fig.clear()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    plt.imshow(environment)

    #Plot the agents
    for i in range(n_agents):
        plt.scatter(agents[i].x, agents[i].y, color='black')
    # Plot the agent with the largest x in red
    lx = max(agents, key=operator.attrgetter('x'))
    plt.scatter(lx.x, lx.y, color='red')
    # Plot the agent with the smallest x in blue
    sx = min(agents, key=operator.attrgetter('x'))
    plt.scatter(sx.x, sx.y, color='blue')
    # Plot the agent with the largest y in yellow
    ly = max(agents, key=operator.attrgetter('y'))
    plt.scatter(ly.x, ly.y, color='yellow')
    # Plot the agent with the smallest y in green
    sy = min(agents, key=operator.attrgetter('y'))
    plt.scatter(sy.x, sy.y, color='green')
    
    global ite
    filename = '../../data/output/images/image' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show()
    #plt.close()
    images.append(imageio.imread(filename))
    return fig

def update(frames):
    '''
    The main model loop

    Parameters
    ----------
    frames : Integer
        The number of frames in the animation.

    Returns
    -------
    None.

    '''
    
    # Model loop
    global carry_on

    # Model loop
    # for ite in range(n_iterations):
    print("Iteration", frames)
    
    # Move agents
    print("Move and Eat")
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max) # move the agent
        agents[i].eat() # allow the agent to eat 
        
    # Share store
    print("Share")
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
    # print("Sum environment", sum_e)
    sum_as = sum_stores(n_agents)
    # print("Sum agent stores", sum_as)
    # print("Total resource", sum_e + sum_as)
    
    # Stopping condition
    # Stop when the average agent store exceeds 80
    if sum_as / n_agents > 80:
        carry_on = False
        print("Stopping Condition: average agent store = ", sum_as / n_agents)
        print("Iterations Run = ", frames)
        
    # Plot
    global ite
    plot()
    # ite = ite + 1 (removed to get rid of issue with only every other plot generated)
    
def gen_function():
    '''
    Passes the iteration variable back whilst continuing to run the while loop.
    Writes the output data to a file, and the images to a GIF

    Returns
    -------
    None.

    '''
    global ite
    global carry_on # Not actually needed as we're not assigning, but clearer
    
    while (ite < n_iterations) & (carry_on):
        yield ite # Returns control and waits for next call.
        ite = ite + 1
    
    global data_written
    if data_written == False:
        # Write data
        # Set the write data menu to normal
        menu_0.entryconfig("Write data", state = "normal")
        data_written = True


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
    
#    for ite in range(n_iterations):
#        # Call the main model loop
#        update(ite)    
    # For storing global images
    global ite
    ite = 0
    images = []

    # Create directory to write images to
    try:
        os.makedirs('../../data/output/images')
    except FileExistsError:
        print("Path exists")

    # Animate
    # Initialise fig and carry_on
    fig = plt.figure(figsize = (7,7))
    ax = fig.add_axes([0, 0, 1, 1])
    carry_on = True
    data_written = False

    # GUI
    root = tk.Tk()
    root.wm_title("Agent Based Model")
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root)
    canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    menu_bar = tk.Menu(root)
    root.config(menu = menu_bar)
    menu_0 = tk.Menu(menu_bar)
    menu_bar.add_cascade(label = "Model", menu = menu_0)
    menu_0.add_command(label = "Run model", command = lambda: run(canvas))
    menu_0.add_command(label = "Write data", command = lambda: output())
    menu_0.add_command(label = "Exit", command = lambda: exiting())
    menu_0.entryconfig("Write data", state = "disabled")
    # Exit if the window is closed
    root.protocol('WM_DELETE_WINDOW', exiting)
    tk.mainloop()
    
    # Calculate the total resource and stores at the start
    total_resource = sum_environment(environment,n_rows,n_cols)
    total_stores = sum_stores(n_agents)
    total_at_start = total_resource + total_stores
    
    #start = time.perf_counter() # record start time
    #maximum_distance = get_max_distance(agents) # call maximum distance calculation
    #end = time.perf_counter() # record end time
    #print("Time take to calculate max distance", end - start, "seconds")
    #print("Maximum distance between agents at initialisation", maximum_distance)
    
        
    
    