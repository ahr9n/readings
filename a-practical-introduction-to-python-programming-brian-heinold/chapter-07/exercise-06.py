# 6. Create the following lists using a for loop.
# (a) A list consisting of the integers 0 through 49
# (b) A list containing the squares of the integers 1 through 50.
# (c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.

L1, L2, L3 = [], [], []

for i in range(50):
    L1.append(i)
for i in range(1, 51):
    L2.append(i ** 2)
for i in range(26):
    L3.append(chr(97 + i) * (i + 1))

print(L1)
print(L2)
print(L3)
