# 3. People often forget closing parentheses when entering formulas. Write a program that asks
# the user to enter a formula and prints out whether the formula has the same number of open-
# ing and closing parentheses.

s = input("Enter a string: ")

opening = s.count("(")
closing = s.count(")")

if opening == closing:
    print("Closing parentheses in the string are equal to the opening ones.")
else:
    print("Closing parentheses in the string are not equal to the opening ones.")
