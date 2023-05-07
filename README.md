# GEOG_5003
Repository for GEOG_5003

The repository consists of the following directories

src
===
Contains the source code to run an Agent Based Model


data
====
Contains input and output data for the Agent Based Model


The Agent Based Model
=====================
There are 9 versions of the model.
The current version of the model is ABM9.
The environment is initialised using input data contained in "../../data/input/in.txt"
The agent locations within the environment are initialised by offsetting data at the following location https://agdturner.github.io/resources/abm9/data.html
Within each iteration of the model, the agents will move randomly, taking resource from the environment and sharing it between them.
The model will run for a given number of iterations, or until the average agent store exceeds a given level.

To run the model, run model2.py. This opens an Agent Based Model GUI - from the menu select Model - Run model
An animation of the agents moving within the environment will run

Once the model has been run, to store the final environment to a file and store the animation to a GIF, from the menu select Model - Write data
The output files will be written to ../../data/output/

To exit the model, select Model - Exit, or close the Agent Based Model window using the X. Console output will be written to ../../data/output/console_op.txt


