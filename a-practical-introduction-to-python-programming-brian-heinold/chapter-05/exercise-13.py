# 13. In the last chapter there was an exercise that asked you to create a multiplication game for
# kids. Improve your program from that exercise to keep track of the number of right and
# wrong answers. At the end of the program, print a message that varies depending on how
# many questions the player got right.

from random import randint

wins = 0
for i in range(1, 11):
    a = randint(1, 100)  # for kids ;)
    b = randint(1, 100)
    print("Question ", i, ": ", a, " x ", b, " = ", sep="", end="")

    c = eval(input())
    if a * b == c:
        print("Right!")
        wins += 1
    else:
        print("Wrong. The answer is", a * b)

print("You have answered", wins, "questions right.")
