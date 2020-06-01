# Resources: 
# 1. https://cs231n.github.io/python-numpy-tutorial/
# 2. https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
# 3. https://numpy.org/install/
# 4. https://python-poetry.org/docs/
# Numpy
# Numpy is the core library for scientific computing in Python. It provides a 
# high-performance multidimensional array object, and tools for working with these arrays.

# Arrays
# A numpy array is a grid of values, all of the same type, and is indexed by a tuple of 
# nonnegative integers. The number of dimensions is the rank of the array; the shape of 
# an array is a tuple of integers giving the size of the array along each dimension.

# We can initialize numpy arrays from nested Python lists, and access elements using square brackets:

import numpy as np

a = np.array([1, 2, 3])         # Create a rank 1 array
print(type(a))                  # prints "<Class 'numpy.ndarray'>"
print(a.shape)                  # prints ("3,")
print(a[0], a[1], a[2])         # prints "1 2 3"

# This stuff finally worked