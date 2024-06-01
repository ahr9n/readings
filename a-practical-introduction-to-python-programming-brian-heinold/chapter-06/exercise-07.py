# 7. Write a program that asks the user to enter a word and determines whether the word is a
# palindrome or not. A palindrome is a word that reads the same backwards as forwards.

s = input("Enter a string: ")

new_string = s[::-1]  # a negative step reverses the string

if s == new_string:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
