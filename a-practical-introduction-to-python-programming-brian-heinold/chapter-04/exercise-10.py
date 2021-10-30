# 10. Write a multiplication game program for kids. The program should give the player ten ran-
# domly generated multiplication questions to do. After each, the program should tell them
# whether they got it right or wrong and what the correct answer is.

# Question 1: 3 x 4 = 12
# Right!
# Question 2: 8 x 6 = 44
# Wrong. The answer is 48.
# ...
# ...
# Question 10: 7 x 7 = 49
# Right.

from random import randint

for i in range(1, 11):
    a = randint(1, 100)  # for kids ;)
    b = randint(1, 100)
    print('Question ', i, ': ', a, ' x ', b, ' = ', sep='', end='')
    
    c = eval(input())
    if a * b == c:
        print('Right!')
    else:
        print('Wrong. The answer is', a * b)
