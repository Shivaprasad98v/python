# Write a Python program to enter a number and print its reverse.

num = 12345
rev = 0

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
    
print ("The reverse number is:", str(rev))
