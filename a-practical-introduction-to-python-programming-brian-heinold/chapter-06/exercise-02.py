# 2. A simple way to estimate the number of words in a string is to count the number of spaces
# in the string. Write a program that asks the user for a string and returns an estimate of how
# many words are in the string.

s = input("Enter a string: ")

words = s.count(" ") + 1
print("Total number of words in string:", words)
