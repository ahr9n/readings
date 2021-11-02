# 14. This exercise is about the well-known Monty Hall problem. In the problem, you are a con-
# testant on a game show. The host, Monty Hall, shows you three doors. Behind one of those
# doors is a prize, and behind the other two doors are goats. You pick a door. Monty Hall, who
# knows behind which door the prize lies, then opens up one of the doors that doesn’t contain
# the prize. There are now two doors left, and Monty gives you the opportunity to change your
# choice. Should you keep the same door, change doors, or does it not matter?
#
# (a) Write a program that simulates playing this game 10000 times and calculates what per-
# centage of the time you would win if you switch and what percentage of the time you
# would win by not switching.
# (b) Try the above but with four doors instead of three. There is still only one prize, and
# Monty still opens up one door and then gives you the opportunity to switch.

from random import randint, choice

# Simulating playing the game 10000 times with 3 doors
switch_cnt, cnt = 0, 0

for i in range(1000):
    guess, prize = randint(1, 3), randint(1, 3)
    if guess == prize:  # don't switch
        cnt += 1

    # switch
    closed_doors = [prize]
    if prize == 1:
        closed_doors.append(choice([2, 3]))
    elif prize == 2:
        closed_doors.append(choice([1, 3]))
    elif prize == 3:
        closed_doors.append(choice([1, 2]))
    # now, we have two closed doors, including the first guess door

    if guess == closed_doors[1]:
        guess = closed_doors[0]  # switch from the first guess

    if guess == prize:
        switch_cnt += 1

percentage, switch_percentage = round((cnt / 1000) * 100, 2), round((switch_cnt / 1000) * 100, 2)
print('With three doors:')
print('Percentage of the time you would win by not switching is:', percentage)
print('Percentage of the time you would win if you switch is:', switch_percentage)

# Simulating playing the game 10000 times with 4 doors
switch_cnt, cnt = 0, 0

for i in range(1000):
    guess, prize = randint(1, 4), randint(1, 4)
    if guess == prize:  # don't switch
        cnt += 1

    # switch
    closed_doors = [prize]
    if prize == 1:
        closed_doors.append(choice([2, 3, 4]))

        if closed_doors[1] == 2:
            closed_doors.append(choice([3, 4]))
        elif closed_doors[1] == 3:
            closed_doors.append(choice([2, 4]))
        else:  # closed_doors[1] == 4:
            closed_doors.append(choice([2, 3]))

    elif prize == 2:
        closed_doors.append(choice([1, 3, 4]))

        if closed_doors[1] == 1:
            closed_doors.append(choice([3, 4]))
        elif closed_doors[1] == 3:
            closed_doors.append(choice([1, 4]))
        else:  # closed_doors[1] == 4:
            closed_doors.append(choice([1, 3]))

    elif prize == 3:
        closed_doors.append(choice([1, 2, 4]))

        if closed_doors[1] == 1:
            closed_doors.append(choice([2, 4]))
        elif closed_doors[1] == 2:
            closed_doors.append(choice([1, 4]))
        else:  # closed_doors[1] == 4:
            closed_doors.append(choice([1, 2]))

    else:  # closed_door[0] == 4:
        closed_doors.append(choice([1, 2, 3]))

        if closed_doors[1] == 1:
            closed_doors.append(choice([2, 3]))
        elif closed_doors[1] == 2:
            closed_doors.append(choice([1, 4]))
        else:  # closed_doors[1] == 3:
            closed_doors.append(choice([1, 2]))

    # now, we have two closed doors, including the first guess door
    if guess == closed_doors[1]:
        guess = closed_doors[0]  # switch from the first guess

    if guess == prize:
        switch_cnt += 1

percentage, switch_percentage = round((cnt / 1000) * 100, 2), round((switch_cnt / 1000) * 100, 2)
print('With four doors:')
print('Percentage of the time you would win by not switching is:', percentage)
print('Percentage of the time you would win if you switch is:', switch_percentage)

# nice explanation for the game: https://www.youtube.com/watch?v=4Lb-6rxZxx0
