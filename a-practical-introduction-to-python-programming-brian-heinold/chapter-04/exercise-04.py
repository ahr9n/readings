# 4. Write a program that asks the user how many credits they have taken. If they have taken 23
# or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.

credit = eval(input('How many credits have you taken? '))

if credit <= 23:
    print('The student is a freshman.')
elif 24 <= credit <= 53:  # Power of Python :)
    print('The student is a sophomore.')
elif 54 <= credit <= 83:
    print('The student is a junior.')
elif credit >= 84:
    print('The student is a senior.')
