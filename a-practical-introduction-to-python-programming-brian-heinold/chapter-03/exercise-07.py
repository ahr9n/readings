# 7. Write a program that asks the user to enter an angle between −180◦ and 180◦. Using an
# expression with the modulo operator, convert the angle to its equivalent between 0◦ and
# 360◦.

angle = eval(input("Enter an angle between −180◦ and 180◦: "))

if angle < 0:
    angle %= 360  # or: += 360 (aka fixing mod)

print(angle)
