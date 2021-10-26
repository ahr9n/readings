# 6. Write a program that asks the user to enter two numbers, x and y, and computes |x − y| / (x + y).

x = eval(input('Enter the number x: '))
y = eval(input('Enter the number y: '))

z = abs(x - y) / (x + y)
print('|x − y| / (x + y) =', z)
