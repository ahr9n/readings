# 5. Write a program that asks the user to enter a number and prints the sum of the divisors of
# that number. The sum of the divisors of a number is an important function in number theory.

import math
number = eval(input('Enter a number: '))
sum = 0

# Efficient algorithm. Time Complexity: O(sqrt(n)).
# See: awesome-reading/a-practical-introduction-to-python-programming-brian-heinold/chapter-04/exercise-09.py
root = math.floor(math.sqrt(number))
for i in range(1, root + 1):
    if number % i == 0:
        sum += i
        if (number // i) != i:
            sum += number // i

print('The sum of the divisors of', number, 'is', sum)
