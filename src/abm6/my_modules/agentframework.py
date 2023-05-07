# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:26:39 2023

@author: ljper
"""
#Imports
import random
import my_modules.geometry as geometry


class Agent():
    def __init__(self, agents, i, environment, n_rows, n_cols):
        """
        The constructor method.
        
        Parameters
        agents : List
            A list of Agent instances
        i : Integer
            To be unique to each instance.
        environment : List
            A reference to a shared environment
        n_rows : Integer 
            The number of rows in the environment
        n_cols : Integer 
            The number of columns in the environment

        Returns
        -------
        None.

        """
        self.agents = agents
        self.i = i
        self.environment = environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1) # initialise somewhere central
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1) # Initialise somewhere central
        self.store = random.randint(0, 99) # randomly initialise the agent's store
        self.store_shares = 0
        
    def __str__(self):
        return self.__class__.__name__ + "(i=" + str(self.i) + ", x=" + str(self.x) + ", y=" + str(self.y) + ")"
    
    def __repr__(self):
        return str(self)
    
    def move(self, x_min, y_min, x_max, y_max):
        # x co-ordinate
        rn = random.random()
        if rn < 0.5:
            self.x = self.x + 1
        else:
            self.x = self.x - 1
        
        # y co-ordinate
        rn = random.random()
        if rn < 0.5:
            self.y = self.y + 1
        else:
            self.y = self.y - 1

        # Apply constraints
        if self.x < x_min:
            self.x = x_min
        if self.y < y_min:
            self.y = y_min
        if self.x > x_max:
            self.x = x_max
        if self.y > y_max:
            self.y = y_max
            
            
    def eat(self):
        '''
        If the environment at the current location is >= 10, transfer 10 from the environment to the agent's store.
        If the agent's store exceeds 100, release half the store back to the environment'
        
        Parameters
        ----------
        None.

        Returns
        -------
        None.

        '''
        #print(self.environment[self.y][self.x], self.store)
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10 # decrement the environment by 10
            self.store += 10 # increment the store by 10
        else:
            self.store += self.environment[self.y][self.x] # increment the store by what is left in the environment
            self.environment[self.y][self.x] = 0 # the environment is now depleted
        #print(self.environment[self.y][self.x], self.store)
        
        # Check whether the agent's store exceeds the limit
        if self.store > 100:
            #print("Big store", self.store)
            # Release half the store back to the environment
            self.environment[self.y][self.x] += self.store / 2
            self.store = self.store / 2
            #print("Little store", self.store)
        
            

    def share(self, neighbourhood):
        '''
        Find other agents within the neighbourhood and share resources between them
        
        Parameters
        ----------
        neighbourhood : Integer
            The distance within which resources will be shared.

        Returns
        -------
        None.

        '''
        
        # Create a list of agents in neighbourhood
        neighbours = []
        for a in self.agents:
            distance = geometry.get_distance(a.x, a.y, self.x, self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)
                
        # Calculate how much to share
        n_neighbours = len(neighbours)
        #print("n_neighbours", n_neighbours)
        shares = self.store / n_neighbours
        #print("shares", shares)
        # Add shares to store_shares
        for i in neighbours:
            self.agents[i].store_shares += shares
