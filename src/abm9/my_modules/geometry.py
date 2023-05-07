# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 08:54:54 2023

@author: zzz03g
"""
import math

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

