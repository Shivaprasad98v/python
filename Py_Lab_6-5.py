# Write a Python program to swap the first and last digits of a number.

num = 12345
l1 = num % 10
while num != 0:
    f1 = num
    num //= 10
print ("The swapped first digit of the number is: ", f1)
print ("The swapped last digit of the number is: ", l1)
