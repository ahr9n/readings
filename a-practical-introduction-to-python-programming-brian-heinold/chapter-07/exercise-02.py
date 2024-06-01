# 2. Write a program that generates a list of 20 random numbers between 1 and 100.
# (a) Print the list.
# (b) Print the average of the elements in the list.
# (c) Print the largest and smallest values in the list.
# (d) Print the second largest and second smallest entries in the list
# (e) Print how many even numbers are in the list.

import random

L = []
for i in range(20):
    L.append(random.randint(1, 100))

print("The list is:", L)
print("Average:", sum(L) / len(L))

L.sort()
print("Largest:", L[-1])
print("Smallest:", L[0])
print("Second largest:", L[-2])
print("Second smallest:", L[1])

even = 0
for i in L:
    if i % 2 == 0:
        even += 1
print("Even numbers:", even)
