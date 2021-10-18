# Use a for loop to print an upside down triangle like the one below. Allow the user to specify
# how high the triangle should be.
# ****
# ***
# **
# *

# How high should the triangle be? 4

high = eval(input('How high should the triangle be? '))

for i in range(high, 0, -1):
    wide = i
    print('*' * wide)
