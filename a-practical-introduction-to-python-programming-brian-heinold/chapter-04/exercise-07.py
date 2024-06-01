# 7. Write a program that asks the user for two numbers and prints 'Close' if the numbers are
# within .001 of each other and 'Not close' otherwise.

num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))

if abs(num1 - num2) <= 0.001:
    print("Close")
else:
    print("Not close")
