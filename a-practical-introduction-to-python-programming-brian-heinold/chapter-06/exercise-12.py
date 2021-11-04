# 12. Write a program that asks the user to enter a word and then capitalizes every other letter of
# that word. So, if the user enters the word 'rhinoceros', the program should print out 'rHiNoCeRoS'.

word = input('Enter a word: ')
for i in range(len(word)):
    if i % 2 == 1:
        print(word[i].upper(), end='')
    else:
        print(word[i], end='')
        
