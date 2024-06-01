# 16. Below is described how to find the date of Easter in any year. Despite its intimidating appear-
# ance, this is not a hard problem. Note that ⌊x⌋ is the floor function, which for positive numbers
# just drops the decimal part of the number. For instance ⌊3.14⌋ = 3. The floor function is part
# of the math module.
# C = century (1900’s → C = 19)
# Y = year (all four digits)
# m = (15 + C − ⌊C/4⌋ − ⌊(8C+13)/25⌋) mod 30
# n = (4 + C − ⌊C/4⌋) mod 7
# a = Y mod 4
# b = Y mod 7
# c = Y mod 19
# d = (19c + m) mod 30
# e = (2a + 4b + 6d + n) mod 7
# Easter is either March (22 + d + e) or April (d + e − 9) There is an exception if d = 29 and e = 6.
# In this case, Easter falls one week earlier on April 19. There is another exception if d = 28,
# e = 6, and m = 2, 5, 10, 13, 16, 21, 24, or 39. In this case, Easter falls one week earlier on April
# 18. Write a program that asks the user to enter a year and prints out the date of Easter in that
# year. (See Tattersall, Elementary Number Theory in Nine Chapters, 2nd ed., page 167)

import math

y = eval(input("Enter a year: "))  # 2021
c = (y // 100) % 100  # 20

m = (15 + c - math.floor(c / 4) - math.floor((8 * c + 13) / 25)) % 30
n = (4 + c - math.floor(c / 4)) % 7
a = y % 4
b = y % 7
c = y % 19
d = (19 * c + m) % 30
e = (2 * a + 4 * b + 6 * d + n) % 7

easter1 = 22 + d + e
avail1 = 0
if easter1 >= 1 and easter1 <= 31:
    avail1 = 1

easter2 = d + e - 9
avail2 = 0
if easter2 >= 1 and easter2 <= 30:
    avail2 = 1

if d == 29 and e == 6:
    print("Easter falls on April 19.")
elif d == 28 and e == 6 and m in [2, 5, 10, 13, 16, 21, 24, 39]:
    print("Easter falls on April 18.")
else:
    if (
        avail1 and avail2
    ):  # # I think it is impossible, yet I am not interested in timing ;)
        print("Easter falls on either March", easter1, "or April", easter2)
    elif avail1:
        print("Easter falls on March", easter1)
    else:
        print("Easter falls on April", easter2)
