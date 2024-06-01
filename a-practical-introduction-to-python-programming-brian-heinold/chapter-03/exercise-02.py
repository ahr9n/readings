# 2. Write a program that generates a random number, x, between 1 and 50, a random number y
# between 2 and 5, and computes pow(x, y).

from random import randint

x = randint(1, 50)  # base
y = randint(2, 5)  # exp or power
z = x**y  # same as pow(x, y)

print("Base:", x)
print("Power:", y)
print("Result:", z)
