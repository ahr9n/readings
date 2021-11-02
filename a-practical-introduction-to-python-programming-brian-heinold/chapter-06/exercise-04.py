# 4. Write a program that asks the user to enter a word and prints out whether that word contains
# any vowels.

s = input('Enter a word: ')

flag = False
for c in s:
    if c in 'aeiou':
        flag = True

if flag:
    print('It contains vowels.')
else:
    print('It doesn\'t contain any vowels')
