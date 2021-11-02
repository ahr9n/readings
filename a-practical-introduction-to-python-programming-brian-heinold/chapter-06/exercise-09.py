# 9. Ask the user for a number and then print the following, where the pattern ends at the number
# that the user enters.
# 1
#  2
#   3
#    4

number = eval(input('Enter a number: '))

for i in range(1, 1 + number):
    print(' ' * i, i)
