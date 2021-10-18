# Use a for loop to print a box like the one below. Allow the user to specify how wide and how
# high the box should be.
# *******************
# *                 *
# *                 *
# *******************

# How wide should the box be? 19
# How high should the box be? 4

wide = eval(input('How wide should the box be? '))
high = eval(input('How high should the box be? '))

if high <= 2:
    print('*' * wide)
    if high == 2:
        print('*' * wide)

else:
    print('*' * wide)
    for i in range(2, high):
        if wide <= 2:
            print('*', end='')
            if wide == 2:
                print('*', end='')
            print('')
        else:
            print('*', end='')
            print(' ' * (wide - 2), end='')
            print('*')
    print('*' * wide)

# You should use 'if conditions' to handle corner cases :)
