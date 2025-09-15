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
def problem2():
    """
    Perform array operations using broadcasting.
    """
    # Given arrays
    arr_a = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
    arr_b = np.array([10, 20, 30])
    # a) Add arr_b to each row of arr_a (using broadcasting)
    result_add = arr_a + arr_b # TODO: Replace None with your code
    # b) Multiply each column of arr_a by the corresponding element in arr_b
    result_multiply = arr_a * arr_b # TODO: Replace None with your code
    # c) Calculate the square of all elements in arr_a
    result_square = arr_a ** 2 # TODO: Replace None with your code
    # d) Calculate the mean of each column in arr_a
    column_means = np.mean(arr_a,axis=0) # TODO: Replace None with your code
    # e) Subtract the column means from each element in the respective column
    # This is called "centering" the data
    centered_arr = arr_a - column_means # TODO: Replace None with your code
    return result_add, result_multiply, result_square, column_means, centered_arr
# Test your function
# Expected output for result_add:
# [[11 22 33]
# [14 25 36]
# [17 28 39]]
print(problem2())
def problem3():
    """
    Demonstrate array indexing and slicing.
    """
    # Create a 5x5 array with values from 1 to 25
    arr = np.arange(1, 26).reshape(5, 5)
    # a) Extract the third row
    third_row = arr[2,:] # TODO: Replace None with your code
    # b) Extract the last column
    last_column = arr[:,-1] # TODO: Replace None with your code
    # c) Extract the 2x2 subarray from the center (rows 1-2, columns 1-2)
    center_subarray = arr[1:3,1:3] # TODO: Replace None with your code
    # d) Extract all elements greater than 15
    greater_than_15 = (arr > 15) # TODO: Replace None with your code
    # e) Replace all even numbers with -1 (create a copy first)
    arr_copy = arr.copy()
    arr_copy[arr_copy % 2 == 0] = -1
    # TODO: Replace even numbers with -1 in arr_copy
    return third_row, last_column, center_subarray, greater_than_15, arr_copy
    # Test your function
print(problem3())
def problem4():
    """
    Perform statistical analysis on student scores.
    """
    # Student test scores (rows: students, columns: tests)
    scores = np.array([[85, 90, 78, 92],
    [79, 85, 88, 91],
    [92, 88, 95, 89],
    [75, 72, 80, 78],
    [88, 91, 87, 94]])
    # a) Calculate the average score for each student (across all tests)
    student_averages = np.mean(scores, axis=1) # TODO: Replace None with your code
    # b) Calculate the average score for each test (across all students)
    test_averages = np.mean(scores, axis=0) # TODO: Replace None with your code
    # c) Find the highest score for each student
    student_max_scores = np.max(scores, axis=1) # TODO: Replace None with your code
    # d) Find the standard deviation of scores for each test
    test_std = np.std(scores, axis=0) # TODO: Replace None with your code
    # e) Identify which students have an average score above 85
    # Return a boolean array
    high_performers = student_averages > 85 # TODO: Replace None with your code
    return student_averages, test_averages, student_max_scores, test_std, high_performers
    # Test your function
    # Expected outputs:
    # student_averages: [86.25, 85.75, 91.0, 76.25, 90.0]
    # test_averages: [83.8, 85.2, 85.6, 88.8]
print(problem4())
def problem6():
    """
    Compare performance between NumPy arrays and Python lists.
    Complete the timing comparisons.
    """
    import time
    size = 100000
    # Create Python list and NumPy array with same data
    python_list = list(range(size))
    numpy_array = np.arange(size)
    # Task: Square all elements
    # Python list approach
    start_time = time.time()
    # TODO: Square all elements in python_list using list comprehension
    list_result = []
    for x in python_list: list_result.append(x**2) # Replace with your code
    list_time = time.time() - start_time
    # NumPy array approach
    start_time = time.time()
    # TODO: Square all elements in numpy_array using NumPy operations
    array_result = numpy_array **2 # Replace with your code
    numpy_time = time.time() - start_time
    # Calculate speedup
    speedup = list_time / numpy_time
    # Return times and speedup factor
    return {
        'list_time': list_time,
        'numpy_time': numpy_time,
        'speedup': speedup,
        'conclusion': f"NumPy is {speedup:.1f}x faster than Python lists for this operation"
        }
# Test your function
# Expected: NumPy should be significantly faster (10x or more)
print(problem6())
def bonus_challenge():
    """
    Create a simple 10x10 'image' and apply transformations.

    """
    # Create a 10x10 array representing a grayscale image
    # Values should be between 0 (black) and 255 (white)
    image = np.random.randint(0, 256, size=(10, 10))
    # a) Normalize the image (scale values to 0-1 range)
    normalized = image / 255 # TODO: Divide by 255
    # b) Apply brightness adjustment (increase all values by 50, cap at 255)
    brightened =  np.clip(image+50,0,255) # TODO: Add 50 and use np.clip
    # c) Create a negative of the image (invert values)
    negative = 255 - image # TODO: Subtract from 255
    # d) Apply threshold (values > 128 become 255, others become 0)
    thresholded = (image > 128).astype(int) * 255# TODO: Use boolean indexing
    return normalized, brightened, negative, thresholded
print(bonus_challenge())
# Add this at the bottom of your file to test all problems
if __name__ == "__main__":
    print("Problem 1 Results:")
    print(problem1())
    print("\nProblem 2 Results:")
    print(problem2())
    print("\nProblem 3 Results:")
    print(problem3())
    print("\nProblem 4 Results:")
    print(problem4())
    print("\nProblem 6 Results:")
    print(problem6())
    # Uncomment if attempting bonus
    print("\nBonus Challenge Results:")
    print(bonus_challenge())
