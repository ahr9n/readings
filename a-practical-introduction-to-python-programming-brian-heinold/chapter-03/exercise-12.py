# 12. Write a program that asks the user for a number and prints out the factorial of that number.

import math

number = eval(input('Enter a number: '))
result = math.factorial(number)

print('Factorial of', number, 'is', result)
