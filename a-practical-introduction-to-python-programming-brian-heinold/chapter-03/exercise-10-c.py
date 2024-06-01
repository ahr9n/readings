# 10.
# (c) Write a program that asks the user to enter a power and how many digits they want.
# Find the last that many digits of 2 raised to the power the user entered.

import math

power = eval(input("Enter a power: "))
digits = eval(input("How many last digits do you want? "))

last_digits = (2**power) % (10**digits)

# good to show all digits, even with leading zero
number_of_last_digits_without_leading_zero = math.ceil(math.log(last_digits, 10))
needed_leading_zero = digits - number_of_last_digits_without_leading_zero

print(
    "The last ",
    digits,
    " digits of 2 raised to the power ",
    power,
    ": ",
    "0" * needed_leading_zero,
    last_digits,
    sep="",
)
