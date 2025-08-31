# Write a Python programming to display a bar chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "Javascript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

plt.bar(languages, popularity, color=['violet', 'blue', 'green', 'yellow', 'orange', 'red'])

plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")
plt.legend(["Bar"])
plt.show()

