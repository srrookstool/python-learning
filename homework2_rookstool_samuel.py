# Required import for all problems
import numpy as np
# Set random seed for reproducible results
np.random.seed(1350) # Use course number as seed
def problem1():
    """
    Complete the following tasks:
    """
    # a) Create a 1D array of integers from 10 to 50 (inclusive) with step 5
    # Store in variable 'arr1'
    arr1 = np.arange(10,51)
    # b) Create a 2D array of shape (3, 4) filled with zeros
    # Store in variable 'arr2'
    arr2 = np.zeros((3,4)) # TODO: Replace None with your code
    # c) Create a 3x3 identity matrix
    # Store in variable 'identity'
    identity = np.eye(3,3) # TODO: Replace None with your code
    # d) Create an array of 10 evenly spaced numbers between 0 and 5
    # Store in variable 'linspace_arr'
    linspace_arr = np.linspace(0,5,10) # TODO: Replace None with your code
    # e) Create a random array of shape (2, 5) with values between 0 and 1
    # Store in variable 'random_arr'
    random_arr = np.random.rand(2,5) # TODO: Replace None with your code
    return arr1, arr2, identity, linspace_arr, random_arr
# Test your function
# Expected outputs (approximately):
# arr1: [10 15 20 25 30 35 40 45 50]
# arr2: 3x4 array of zeros
# identity: 3x3 identity matrix
# linspace_arr: 10 evenly spaced values from 0 to 5
# random_arr: 2x5 array with random values
print(problem1())
