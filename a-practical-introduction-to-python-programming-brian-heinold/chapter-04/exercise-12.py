# 12. A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly
# how much candy is in the bowl, then you win all the candy. You ask the person in charge the
# following: If the candy is divided evenly among 5 people, how many pieces would be left
# over? The answer is 2 pieces. You then ask about dividing the candy evenly among 6 people,
# and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among
# 7 people, and the amount left over is 2 pieces. By looking at the bowl, you can tell that there
# are less than 200 pieces. Write a program to determine how many pieces are in the bowl.

among5 = eval(
    input("Would the candy be divided evenly among 5 people? Yes (1) or No (2)? ")
)
among6 = eval(
    input("Would the candy be divided evenly among 6 people? Yes (1) or No (2)? ")
)
among7 = eval(
    input("Would the candy be divided evenly among 7 people? Yes (1) or No (2)? ")
)

found = 0
for i in range(1, 200):
    flag5 = (i % 5 == 0 and among5 == 1) or (i % 5 != 0 and among5 == 2)
    flag6 = (i % 6 == 0 and among6 == 1) or (i % 6 != 0 and among6 == 2)
    flag7 = (i % 7 == 0 and among7 == 1) or (i % 7 != 0 and among7 == 2)

    if flag5 and flag6 and flag7:
        if found:
            print(" or", i, end="")
        else:
            print("Pieces of candy could be:", i, end="")
        found = 1

if not found:
    print("Impossible to guess.")
