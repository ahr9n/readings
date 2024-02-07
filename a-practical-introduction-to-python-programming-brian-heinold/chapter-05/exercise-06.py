# 6. A number is called a perfect number if it is equal to the sum of all of its divisors, not including
# the number itself. For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6
# and 6 = 1 + 2 + 3. As another example, 28 is a perfect number because its divisors are 1, 2, 4,
# 7, 14, 28 and 28 = 1 + 2 + 4 + 7 + 14. However, 15 is not a perfect number because its divisors
# are 1, 3, 5, 15 and 15 != 1 + 3 + 5. Write a program that finds all four of the perfect numbers
# that are less than 10000.

import math

print('Perfect numbers are:')
# Efficient algorithm. Time Complexity: O(sqrt(n)).
# See: readings/a-practical-introduction-to-python-programming-brian-heinold/chapter-04/exercise-09.py

for number in range(1000, 10000):  # four less than 10000
    root, div_sum = math.floor(math.sqrt(number)), 0
    for i in range(1, root + 1):
        if number % i == 0:
            div_sum += i
            if (i // number) != number:
                div_sum += number // i

    div_sum -= number
    if div_sum == number:
        print(number)
