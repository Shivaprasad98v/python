# Find common items from two lists

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

common = list(set(a) & set(b))

print(common)
