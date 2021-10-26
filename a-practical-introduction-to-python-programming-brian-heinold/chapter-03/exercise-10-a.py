# 10.
# (a) One way to find out the last digit of a number is to mod the number by 10. Write a
# program that asks the user to enter a power. Then find the last digit of 2 raised to that
# power.

power = eval(input('Enter a power: '))

last_digit = (2 ** power) % 10
print('The last digit of 2 raised to that power is:', last_digit)

# Another tricky solution for LARGE powers:
# 1. You don't need to get the all real number of (2 ** power)
# 2. You can see if there is a pattern (of the last digit of the powers of two) to follow

# power:result:last_digit
# 0    :1     :1
# 1    :2     :2
# 2    :4     :4
# 3    :8     :8
# 4    :16    :6
# 5    :32    :2
# 6    :64    :4
# 7    :128   :8
# 8    :256   :6
# 9    :512   :2
# 10   :1024  :4

# You will see now the (2, 4, 8, 6) pattern, and yes, it will continue like this!
# So, simply the answer will be:

# if power == 0:
#     print('1')
# else:
#     power -= 1
#     power %= 4
#     if power == 0:
#         print('2')
#     elif power == 1:
#         print('4')
#     elif power == 2:
#         print('8')
#     else:  # power == 3
#         print('6')

# Now, compare the time and memory complexity ;)
