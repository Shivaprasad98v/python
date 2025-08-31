# Write a Python program to remove duplicates from a list.

list_1 = [5, 2, 90, 24, 10, 2, 90, 34]
list_2 = ['a', 'a', 'a', 'b', 'c', 'd', 'd', 'e']

list_1 = list(dict.fromkeys(list_1))
print (list_1)

list_2 = list(dict.fromkeys(list_2))
print (list_2)
