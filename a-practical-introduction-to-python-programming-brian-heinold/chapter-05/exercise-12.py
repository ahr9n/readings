# 12. Write a program that asks the user to guess a random number between 1 and 10. If they guess
# right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
# the user five numbers to guess and print their score after all the guessing is done.

from random import randint

points = 0
for i in range(10):
    number = randint(1, 10)
    guess = eval(input("Guess a number between 1 and 10: "))

    if guess == number:
        points += 10
        print("You are right!")
    else:
        points -= 1
        print("You are wrong.")

print("Your final points:", points)
