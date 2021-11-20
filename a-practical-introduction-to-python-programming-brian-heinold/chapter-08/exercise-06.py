# 6. Write a simple lottery drawing program. The lottery drawing should consist of six different
# numbers between 1 and 48.

import random
# create a list of numbers from 1 to 48
numbers = list(range(1, 49))
lottery_numbers = []
for i in range(6):
    # pick a random number from the list
    number = random.choice(numbers)
    # add the number to the list of lottery numbers
    lottery_numbers.append(number)
    # remove the number from the list to avoid duplicates
    numbers.remove(number)

print(lottery_numbers)
