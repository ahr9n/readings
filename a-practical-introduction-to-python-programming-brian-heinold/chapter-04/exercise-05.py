# 5. Generate a random number between 1 and 10. Ask the user to guess the number and print a
# message based on whether they get it right or not.

from random import randint

number = randint(1, 10)
guess = eval(input("Guess a number between 1 and 10: "))

if number == guess:
    print("You are right!")
else:
    print("You are wrong.")
