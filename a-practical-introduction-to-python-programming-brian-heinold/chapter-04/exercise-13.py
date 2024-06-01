# 13. Write a program that lets the user play Rock-Paper-Scissors against the computer. There
# should be five rounds, and after those five rounds, your program should print out who won
# and lost or that there is a tie.

from random import randint

choice1 = "Rock"
choice2 = "Paper"
choice3 = "Scissors"

wins, ties = 0, 0

for i in range(5):
    computer_choice = randint(1, 3)

    print(
        "Write '1' for "
        + choice1
        + ", '2' for "
        + choice2
        + ", '3' for "
        + choice3
        + ". All without quotes."
    )
    user_choice = eval(input("Enter your choice: "))

    print("Computer chose ", end="")
    if computer_choice == 1:
        print(choice1, end="")
    elif computer_choice == 2:
        print(choice2, end="")
    elif computer_choice == 3:
        print(choice3, end="")
    print(" and you chose ", end="")
    if user_choice == 1:
        print(choice1, end="")
    elif user_choice == 2:
        print(choice2, end="")
    elif user_choice == 3:
        print(choice3, end="")
    print(".\n")

    if computer_choice == user_choice:
        ties += 1
    elif computer_choice == 1 and user_choice == 2:
        wins += 1
    elif computer_choice == 2 and user_choice == 3:
        wins += 1
    elif computer_choice == 3 and user_choice == 1:
        wins += 1

print(ties, wins, 5 - wins - ties)

if wins > 5 - wins - ties:
    print("Yow won!")
elif wins < 5 - wins - ties:
    print("Computer won!")
else:
    print("It is a tie.")

# lists in this solution would be more helpful, but not illustrated yet ;)
