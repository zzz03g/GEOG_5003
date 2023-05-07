# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 11:18:59 2023

@author: ljper
"""

def read_data():
    '''
    Write the content of a CSV file to data, converting to float type

    Returns
    -------
    data_tuple - a tuple containing
        error - boolean flag indicating rows of inequal lengths
        row_count - the number of rows in the data
        column_count - the number of columns in the data
        data - the list of data

    '''
    import csv
    
    row_length = 0
    row_count = 0
    row_error = False
    
    data_tuple = ()
    
    # Read input data
    f = open('../../data/input/in.txt', newline='')
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row_count += 1 # increment row count
        row = [] # initialise row
        for value in line:
            row.append(value) # append all numbers from this row
            #print(value)
        
        # check the rows are all the same length
        if 0 == row_length: # don't check first row
            row_length = len(row)
            data.append(row) # append this row to the end of data
        elif len(row) != row_length:
                row_error = True
        else:
            data.append(row) # append this row to the end of data
    f.close()
    
    # Write to the output
    data_tuple = (row_error, row_count, row_length, data)
    return data_tuple
    
def write_to_file(file, environment):
    '''
    Write the values of the environment to a file

    Parameters
    ----------
    environment : a list 
        The remaining resource at each point in the environment


    Returns
    -------
    None.

    '''
    f = open(file, 'w') # Open the environment file for writing
    
    for line in environment:
        for value in line:
            f.write(str(value))
            f.write('\t')
        f.write('\n')
    f.close()   # close the file    

    