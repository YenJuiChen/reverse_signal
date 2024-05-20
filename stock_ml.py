#!usr/bin/env python
import sys
import numpy as np
import pandas as pd
# Adapted from the following works:
# 1) A Neural Network in 11 lines of Python (Part 1)
# https://iamtrask.github.io/2015/07/12/basic-python-network/
# 2) Creating a Neural Network from Scratch in Python: Adding Hidden Layers
# https://stackabuse.com/creating-a-neural-network-from-scratch-in-python-adding-hidden-layers/
# 3) Building a Feedforward Neural Network from Scratch in Python
# https://hackernoon.com/building-a-feedforward-neural-network-from-scratch-in-python-d3526457156b
# 
# stock_ml.py
# lockeyj | 2021-01-26
# Defintion:
# l0, layer 0 (input layer, i.e. matrix of technical signals)
# sn0, sigmoid neuron zero (hidden layer, generating matrix of synaptic weights)
# l1, layer 1 (output layer, i.e. matrix of decision)
# Input layer from a matrix of bullish and bearish signals
x = np.array([])
inputfile0 = pd.read_table(sys.argv[1], delimiter=' ', header=None)
x = inputfile0.values
# Sigmoid function in the hidden layer
def sigmoid(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# Output layer buy or sell decision
y = np.array([])
inputfile1 = pd.read_table(sys.argv[2], delimiter=' ', header=None)
y = inputfile1.values
# Seed random numbers to make calculation
np.random.seed(1)
# Initialize weights and bias randomly
w = np.random.rand(20,1)
bias = np.random.rand(1)
for epoch in range(1000000):
    # Feedforward
    l0 = x
    syn0 = w
    xw = np.dot(l0,syn0)
    l1 = sigmoid(xw + bias)
    # Backpropagation with the error output
    l1_error = y - l1
    if (epoch% 100000) == 0:
        print ("Error:" + str(np.mean(np.abs(l1_error))))
    l1_delta = l1_error * sigmoid(l1,True)
    # Update the matrix of weights
    syn0 += np.dot(l0.T,l1_delta)
# Print the results
print ("Output after training:")
print (l1)
print ("Weight matrix:")
print (syn0)
# EOF