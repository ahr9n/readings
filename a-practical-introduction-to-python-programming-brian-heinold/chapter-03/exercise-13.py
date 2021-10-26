# 13. Write a program that asks the user for a number and then prints out the sine, cosine, and
# tangent of that number.

import math

number = eval(input('Enter a number: '))

sine = math.sin(number)
cosine = math.cos(number)
tangent = math.tan(number)

print('Sine of', number, 'is', sine)
print('Cosine of', number, 'is', cosine)
print('Tangent of', number, 'is', tangent)

# Degree to radian: number = number / 180 * math.pi
