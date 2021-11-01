# 9. Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect
# cubes, or perfect fifth powers.
import math

cnt = 0
for i in range(1, 1001):
    SQRT = math.ceil(i ** (1 / 2))
    CUBE = math.ceil(i ** (1 / 3))
    FIFTH = math.ceil(i ** (1 / 4))

    perfect_square = (SQRT * SQRT == i)
    perfect_cube = (CUBE * CUBE * CUBE == i)
    perfect_fifth = (FIFTH * FIFTH * FIFTH * FIFTH == i)

    if not perfect_square and not perfect_cube and not perfect_fifth:
        cnt += 1

print(cnt)
