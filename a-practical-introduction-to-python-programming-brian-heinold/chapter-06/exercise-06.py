# 6. Write a program that asks the user to enter a string s and then converts s to lowercase, re-
# moves all the periods and commas from s, and prints the resulting string.

s = input("Enter a string: ")

s = s.lower()
s = s.replace(".", "")  # periods = points

print(s)
