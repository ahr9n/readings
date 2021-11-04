# 18. The goal of this exercise is to see if you can mimic the behavior of the in operator and the
# count and index methods using only variables, for loops, and if statements.
# (a) Without using the in operator, write a program that asks the user for a string and a letter
# and prints out whether or not the letter appears in the string.
# (b) Without using the count method, write a program that asks the user for a string and a
# letter and counts how many occurrences there are of the letter in the string.
# (c) Without using the index method, write a program that asks the user for a string and
# a letter and prints out the index of the first occurrence of the letter in the string. If the
# letter is not in the string, the program should say so.

s = input('Enter a string: ')
l = input('Enter a letter: ')

flag = False
for i in range(len(s)):
    if s[i] == l:
        flag = True
        break
if flag:
    print('The letter is in the string.')
else:    
    print('The letter is not in the string.')

cnt = 0
for i in range(len(s)):
    if s[i] == l:
        cnt += 1
print('The letter appears {} times in the string.'.format(cnt))

idx = -1
for i in range(len(s)):
    if s[i] == l:
        idx = i
        break
if idx != -1:  
    print('The letter is in the string at index {}.'.format(idx))
else:
    print('The letter is not in the string.')
    
