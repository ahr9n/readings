# Write a program that prints a giant letter A like the one below. Allow the user to specify how
# large the letter should be.
#     *
#    * *
#   *****
#  *     *
# *       *

# How large should the letter 'A' be? 5
import math

high = eval(input("How large should the letter 'A' be? "))
# 1 or 2 in input makes no sense in drawing 'A' letter
# 'high' should be larger than 2

line_position = math.ceil((high + 1) / 2)
base = 2 * high - 1

right_spaces = high - 1
middle_spaces = 0

for i in range(high):
    print(" " * right_spaces, end="")
    if i == 0:
        print("*", end="")
    elif i == line_position - 1:
        print("*" * (high + (high % 2 == 0)), end="")
        # even 'high' should be handled to be odd
    else:
        print("*", end="")
        print(" " * middle_spaces, end="")
        print("*", end="")
    print(" " * right_spaces)

    middle_spaces = 2 * (i + 1) - 1
    right_spaces -= 1

# nice handling :)
