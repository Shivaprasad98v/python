# Convert a list of multiple integers into a single integer.

a = [1, 2, 3, 4, 5]
result = 0
 
for num in a:
    result = result * 10 + num
print ("Convertion of a list into a single integer:", result)
