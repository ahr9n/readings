# Use for loops to print a diamond like the one below. Allow the user to specify how high the
# diamond should be.
#     *
#    ***
#   *****
#  *******
#   *****
#    ***
#     *

# How high should the triangle be? 7

import math

high = eval(input('How high should the diamond be? '))

up = math.ceil(high / 2)
base = high - (high % 2 == 0)

asterisks = 1
spaces = base - asterisks
for i in range(up):
    print(' ' * round(spaces / 2), end='')
    print('*' * (2 * asterisks - 1), end='')
    print(' ' * round(spaces / 2))
    spaces -= 2
    asterisks += 1

down = high - up
asterisks -= 1
spaces += 2

if high % 2 == 0:  # repeat the base of the upside pyramid
    print('*' * base)
    down -= 1  # therefore, decrease the downside counter

for i in range(down, 0, -1):
    asterisks -= 1
    spaces += 2
    print(' ' * round(spaces / 2), end='')
    print('*' * (2 * asterisks - 1), end='')
    print(' ' * round(spaces / 2))

# too much logic, yet so simple :)
# I need to use math library, otherwise I could use casting
