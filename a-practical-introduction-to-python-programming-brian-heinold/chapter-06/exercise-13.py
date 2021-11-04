# 13. Write a program that asks the user to enter two strings of the same length. The program
# should then check to see if the strings are of the same length. If they are not, the program
# should print an appropriate message and exit. If they are of the same length, the program
# should alternate the characters of the two strings. For example, if the user enters abcde and
# ABCDE the program should print out AaBbCcDdEe .

first_string = input('Enter a string: ')
second_string = input('Enter another string: ')

if len(first_string) != len(second_string):
    print('The strings are not the same length.')
else:
    for i in range(len(first_string)):
        print(second_string[i] + first_string[i], end='')
