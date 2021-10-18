# Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,
# and 5x, each separated by three dashes, like below.

# Enter a number: 7
# 7---14---21---28---35

x = eval(input('Enter a number: '))

x2 = x + x
x3 = x + x2
x4 = x2 + x2
x5 = x2 + x3

print(x, x2, x3, x4, x5, sep='---')
