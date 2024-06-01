# 7. Write a program that estimates the average number of drawings it takes before the user’s
# numbers are picked in a lottery that consists of correctly picking six different numbers that
# are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of
# user numbers and simulates drawings until the user’s numbers are drawn. Find the average
# number of drawings needed over the 1000 times the loop runs.

import random

lottery_numbers = [i for i in range(1, 11)]

avg = 0
for i in range(1000):
    user = random.randint(1, 10)
    lott = random.choice(lottery_numbers)
    if lott == user:
        avg = avg + 1

print("Average number of drawings:", round(1000 / avg, 4))
