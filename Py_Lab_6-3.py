# Write a Python function program to count a number of digits in a number.

count = 0
num = 92400133

while num != 0:
    num //= 10
    count += 1
    
print ("Total no. of digits in the given number are: ", count)
