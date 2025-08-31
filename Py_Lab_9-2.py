# Write a Pandas program to convert a dictionary to a Pandas series.

import pandas as pd

a = {'g' : 100, 'e' : 200,
     'k' : 400, 's' : 800,
     'n' : 1600}

panda_series = pd.Series(a)

print (panda_series)
