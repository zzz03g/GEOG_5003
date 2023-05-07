# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:18:17 2023

@author: ljper
"""
# imports
import random
import math

# Set the pseudo-random seed for reproducibility
'''random.seed(0)'''

# Initialise variable x0 with a random number between 0 & 99
x0 = random.randint(0,99)
print("x0", x0)

# Initialise variable y0 with a random number between 0 & 99
y0 = random.randint(0,99)
print("y0", y0)

# Change x0 and y0 randomly
rn = random.random()
print("rn", rn)

if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)

rn = random.random()
print("rn", rn)

if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)

# Initialise variable x1 with a random number between 0 & 99
x1 = random.randint(0,99)
print("x1", x1)

# Initialise variable y1 with a random number between 0 & 99
y1 = random.randint(0,99)
print("y1", y1)

# Change x1 and y1 randomly
rn = random.random()
print("rn", rn)

if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print("x1", x1)

rn = random.random()
print("rn", rn)

if rn < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print("y1", y1)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
#test values
''' comment out test values
x0 = 0
y0 = 0
x1 = 3
y1 = 4
'''

xdiff = x0 - x1
ydiff = y0 - y1
xydist = math.sqrt(xdiff**2 + ydiff**2)
print("xydist", xydist)
