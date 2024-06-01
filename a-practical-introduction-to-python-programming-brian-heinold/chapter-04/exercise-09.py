# 9. Write a program that asks the user to enter a number and prints out all the divisors of that
# number. [Hint: the % operator is used to tell if a number is divisible by something. See Section
# 3.2.]

import math

number = eval(input("Enter a number: "))

# Efficient algorithm. Time Complexity: O(sqrt(n))
root = math.floor(math.sqrt(number))
for i in range(1, root + 1):
    if number % i == 0:
        print(i)
        if (number // i) != i:
            print(number // i)

# Non-efficient brute-force algorithm. Time Complexity: O(n)
# for i in range(1, number + 1):
#     if number % i == 0:
#         print(i)
