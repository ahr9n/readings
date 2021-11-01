# 11. Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
# and asks them how many hours into the future they want to go. Print out what the hour will
# be that many hours into the future, printing am or pm as appropriate. An example is shown
# below.

# Enter hour: 8
# am (1) or pm (2)? 1
# How many hours ahead? 5
# New hour: 1 pm

hour = eval(input('Enter an hour: '))
flag = eval(input('am (1) or pm (2)? '))
flag -= 1

# converting first to 24-style makes it easier
if flag == 0 and hour == 12:
    hour = 0
elif flag == 1 and hour != 12:
    hour += 12

hours_ahead = eval(input('How many hours ahead? '))

hour = (hour + hours_ahead) % 24

# now, check the current 24-style ;)
if hour == 0:
    hour = 12
    flag = 0
elif hour >= 12:
    flag = 1
    if hour > 12:
        hour %= 12

print('New hour:', hour, 'ap'[flag] + 'm')
