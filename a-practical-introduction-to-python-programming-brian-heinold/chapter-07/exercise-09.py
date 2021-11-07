# 9. When playing games where you have to roll two dice, it is nice to know the odds of each
# roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about
# 17%. You can compute these mathematically, but if you don’t know the math, you can write
# a program to do it. To do this, your program should simulate rolling two dice about 10,000
# times and compute and print out the percentage of rolls that come out to be 2, 3, 4, ..., 12.

import random

L, rolls_freq = [], []

for i in range(12):
    L.append(i + 1)
    rolls_freq.append(0)

for i in range(10000):
    roll = random.randint(1, 6) + random.randint(1, 6)
    rolls_freq[roll - 1] += 1
    # frequency of rolls

for i in range(1, 12):
    rolls_freq[i] = rolls_freq[i] / 10000
    # probability of rolls
    print('percentage of rolls that come out to be', i + 1, 'is', rolls_freq[i] * 100)
