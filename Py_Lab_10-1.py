# Write a Python program to draw a line with suitable label in the x axis, y axis and a title.

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.plot (x, y)
plt.xlabel ("X-axis")
plt.ylabel ("Y-axis")
plt.title ("Line Graph")
plt.show ()
