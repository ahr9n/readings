# 12. Write a program that generates 100 random integers that are either 0 or 1. Then find the
# longest 'run' of zeros, the largest number of zeros in a row. For instance, the longest run of
# zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

import random

L = []
for i in range(100):
    L.append(random.randint(0, 1))

longest_run = 0
current_run = 0
for i in range(len(L)):
    if L[i] == 0:
        current_run += 1
    else:
        current_run = 0
    longest_run = max(longest_run, current_run)

print(L)
print(longest_run)
