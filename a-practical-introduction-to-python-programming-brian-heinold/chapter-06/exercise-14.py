# 14. Write a program that asks the user to enter their name in lowercase and then capitalizes the
# first letter of each word of their name.

name = input("Enter your name in lowercase: ")
for s in name.split():
    print(s[0].upper() + s[1:], end=" ")
