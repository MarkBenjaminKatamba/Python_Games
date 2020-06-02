# Resources: 
# 1. https://cs231n.github.io/python-numpy-tutorial/
# 2. https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
# 3. https://numpy.org/install/
# 4. https://python-poetry.org/docs/
# 5. https://pythontic.com/visualization/charts/sinewave
# Numpy
# Numpy is the core library for scientific computing in Python. It provides a 
# high-performance multidimensional array object, and tools for working with these arrays.

# Arrays
# A numpy array is a grid of values, all of the same type, and is indexed by a tuple of 
# nonnegative integers. The number of dimensions is the rank of the array; the shape of 
# an array is a tuple of integers giving the size of the array along each dimension.

# We can initialize numpy arrays from nested Python lists, and access elements using square brackets:
'''
import numpy as np

a = np.array([1, 2, 3])         # Create a rank 1 array
print(type(a))                  # prints "<Class 'numpy.ndarray'>"
print(a.shape)                  # prints ("3,")
print(a[0], a[1], a[2])         # prints "1 2 3"

# This stuff finally worked
'''

# Example
import numpy as np
import matplotlib.pyplot as plot


# Get x values of the sine wave
time = np.arange(0, 10, 0.1)


# Amplitude of the sine wave is sine of a variable like time
amplitude = np.sin(time)


# Plot a sine wave of using time and amplitude obtained for the sine wave
plot.plot(time,amplitude)


# Give a title for the sine wave plot 
plot.title('Sine Wave')


# Give x axis label for the sine wave plot
plot.xlabel('Time')


# Give y axis label for the sine wave plot
plot.ylabel('Amplitude = sine(time)')


plot.grid(True, which='both')

plot.axhline(y = 0, color = 'b')

# Display the sine wave
plot.show()