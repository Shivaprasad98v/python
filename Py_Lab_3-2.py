# Write a Python program to check if a string is a palindrome.

str1 = "ICT Department"
rev_str1 = ""
for char in str1:
    rev_str1 = char + rev_str1
if (str1 == rev_str1):
    print (str1, "is palindrome")
else:
    print (str1, "is not palindrome")
