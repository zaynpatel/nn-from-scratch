"""
import sys
#import matplotlib
import numpy as numpy

print("Python: ", sys.version)
print("Numpy : ", sys.version)
print("Matplotlib: ", sys.version)

"""
"""
inputs = [3.4, 5.7, 8.8]
weights = [2.2, 5.5, 3.1]
bias = 4

output = inputs[0] + weights[0] + inputs[1] + weights[1] + inputs[2] + weights[2] + bias 
print(output)
"""


inputs = [1, 2, 3, 2.5]
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
        inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
        inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3]

print(output)



"""
loop through every element of inputs, weights, bias and print out the value for arr1, arr2, arr3

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
bias = [[2], [3], [0.5]]

test_list = []

for out in inputs, weights, bias:
    test_list.append((inputs[out] + weights[out] + bias[out]))

print(test_list)
"""
