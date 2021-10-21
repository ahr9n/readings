# 4. Write a program that generates a random decimal number between 1 and 10 with two decimal
# places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.

import random

number = random.uniform(1.00, 10.00)  # returns a random float number between the range
number = round(number, 2)  # up to 2 decimal places (two decimal places of accuracy)

print(number)

# For more info: https://docs.python.org/3/library/random.html
