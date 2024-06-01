# Write a program that uses exactly four for loops to print the sequence of letters below.

# AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

for i in range(10):
    print("A", end="")

for i in range(7):
    print("B", end="")

for i in range(4):
    print("CD", end="")

print("E", end="")

for i in range(6):
    print("F", end="")

print("G")

# output: AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
