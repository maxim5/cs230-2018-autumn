"""
CS230 Hands-on session 3: Tensorflow tutorial
Kian Katanforoosh, Andrew Ng
"""

import tensorflow as tf

# Load dataset using tensorflows mnist API
### START CODE HERE (Question 1) ###
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
### END CODE HERE (Question 1) ###


# Define placeholder input data  matrix and for the labels
### START CODE HERE (Question 2) ###

### END CODE HERE (Question 2) ###

# Define parameters W and b of your model
### START CODE HERE (Question 3) ###

### END CODE HERE (Question 3) ###

# Define your model's tensorflow graph
### START CODE HERE (Question 4) ###

### END CODE HERE (Question 4) ###

# Compute the cost function
### START CODE HERE (Question 5) ###

### END CODE HERE (Question 5) ###

# Define accuracy metric
### START CODE HERE (Question 6) ###

### END CODE HERE (Question 6) ###


# Define optimization method, learning rate and the the training step
### START CODE HERE (Question 7) ###

### END CODE HERE (Question 7) ###

# Initialize the variables of the graph, create tensorflow session and run the initialization of global variables.
### START CODE HERE (Question 8) ###

### END CODE HERE (Question 8) ###

# Implement the Optimization Loop for 100 iterations
### START CODE HERE (Question 9) ###

### END CODE HERE (Question 9) ###

# Evaluate your accuracy and cost on the train and test sets
### START CODE HERE (Question 10) ###

### END CODE HERE (Question 10) ###


# How can you improve the code? What do you observe?
