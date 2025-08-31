# Write a NumPy program to find common values between two arrays.

import numpy as np

a = np.array ([1, 2, 3, 7, 5])
b = np.array ([1, 2, 4, 3, 6])

print ("The common values between two elements are: ")

for x in a:
    for y in b:
        if x == y:
            print (x)
            