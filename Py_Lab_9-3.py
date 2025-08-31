# Write a Pandas program to create a series from a list, numpy array and dict.

import pandas as pd
import numpy as np

List = [5, 10, 15, 20, 25, 30]

Array = np.array([5, 10, 15, 20, 25, 30])

dic = {
   "A":"demo",
   "B": 40,
   "C": 25,
   "D": "Yes"
}

res = pd.Series(List)
print("Series = \n",res)

res = pd.Series(Array)
print("Series = \n",res)

d = {
   "A":"demo",
   "B": 40,
   "C": 25,
   "D": "Yes"
}

res = pd.Series(dic)
print("Series = \n",res)
