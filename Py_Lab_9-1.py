# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

import pandas as pd

ds1 = pd.Series([2, 4, 6])
ds2 = pd.Series([1, 3, 5])

ds = ds1 + ds2
print("Add two Series:")
print(ds)

ds = ds1 - ds2
print("Subtract two Series:")
print(ds)

ds = ds1 * ds2
print("Multiply two Series:")
print(ds)

ds = ds1 / ds2
print("Divide Series1 by Series2:")
print(ds)
