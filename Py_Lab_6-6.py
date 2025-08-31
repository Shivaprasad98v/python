# Write a Python program to calculate the product of digits of a number.

product = 1
num = 1234

while num != 0:
    product *= (num % 10)
    num //= 10
    
print ("Total product of all the digits is: ", product)
