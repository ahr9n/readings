# Use a for loop to print a box like the one below. Allow the user to specify how wide and how
# high the box should be. [Hint: print('*' * 10) prints ten asterisks.]
# *******************
# *******************
# *******************
# *******************

# How wide should the box be? 19
# How high should the box be? 4

wide = eval(input('How wide should the box be? '))
high = eval(input('How high should the box be? '))

for i in range(high):
    print('*' * wide)
