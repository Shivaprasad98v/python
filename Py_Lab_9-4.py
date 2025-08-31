# Write a Pandas program to stack two series vertically and horizontally.

import pandas as pd

series1 = pd.Series (['g', 'e', 'e', 'k', 's'])
print ("Series 1:")
print (series1)

series2 = pd.Series ([9, 8, 7, 6, 5])
print ("Series 2:")
print (series2)
 
df = pd.concat ([series1, series2], axis = 1)
print ("\nStack two series horizontally:")
print (df)
