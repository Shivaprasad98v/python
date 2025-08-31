# Write a Python program to find the longest word in a sentence.

str1 = "I am from ICT Department"

words = str1.split()

res = ""

for word in words:
    if len(word) > len(res):
        res = word
        
print (res)
    