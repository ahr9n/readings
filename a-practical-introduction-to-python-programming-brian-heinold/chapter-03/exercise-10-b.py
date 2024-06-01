# 10.
# (b) One way to find out the last two digits of a number is to mod the number by 100. Write
# a program that asks the user to enter a power. Then find the last two digits of 2 raised to
# that power.

power = eval(input("Enter a power: "))

last_digits = (2**power) % 100

# good to show two digits, even with leading zero
leading_zero = 0
if last_digits < 10:
    leading_zero += 1

print("The last two digits of 2 raised to that power are: ", end="")
if leading_zero == 1:
    print("0", last_digits, sep="")
else:
    print(last_digits)

# Try to get another tricky solution for LARGE powers by yourself ;)
