# Write a NumPy program to find the memory size of a NumPy array.

import numpy as np

a = np.array ([1, 2, 3, 4, 5])
memory_size = a.size * a.itemsize
print ("Memory size in bytes is: ", memory_size)
