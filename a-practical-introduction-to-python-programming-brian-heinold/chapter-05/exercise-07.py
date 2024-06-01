# 7. An integer is called 'squarefree' if it is not divisible by any perfect squares other than 1. For
# instance, 42 is 'squarefree' because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
# numbers (except 1) is a perfect square. On the other hand, 45 is not 'squarefree' because it is
# divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
# tells them if it is 'squarefree' or not.

import math

number = eval(input("Enter a number: "))

# Efficient algorithm. Time Complexity: O(sqrt(n)).
# See: readings/a-practical-introduction-to-python-programming-brian-heinold/chapter-04/exercise-09.py

flag = True
root = math.floor(math.sqrt(number))
for i in range(2, root + 1):
    if number % i == 0:
        SQRT1 = math.ceil(math.sqrt(i))
        SQRT2 = math.floor(math.sqrt(i))
        if SQRT1 * SQRT1 == SQRT2 * SQRT2:
            flag = False

        if (i // number) != number:
            SQRT1 = math.ceil(math.sqrt(number // i))
            SQRT2 = math.floor(math.sqrt(number // i))
            if SQRT1 * SQRT1 == SQRT2 * SQRT2:
                flag = False

if flag:
    print("It is a 'squarefree'.")
else:
    print("It is not a 'squarefree'.")
