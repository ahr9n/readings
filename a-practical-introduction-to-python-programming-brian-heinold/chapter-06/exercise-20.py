# 20. Write a program that converts a time from one time zone to another. The user enters the time
# in the usual American way, such as 3:48pm or 11:26am. The first time zone the user enters
# is that of the original time and the second is the desired time zone. The possible time zones
# are Eastern, Central, Mountain, or Pacific.
# Time: 11:48pm
# Starting zone: Pacific
# Ending zone: Eastern
# 2:48am

input_time = input('Enter a time in the format hh:mm[am/pm]: ')

hour = int(input_time[0:2])
minute = int(input_time[3:5])

start_zone = input('Enter the starting time zone: ')
end_zone = input('Enter the ending time zone: ')
flag = input_time[5:7]

if (flag != 'am' and flag != 'pm') or start_zone not in ['Eastern', 'Central', 'Mountain', 'Pacific']\
        or end_zone not in ['Eastern', 'Central', 'Mountain', 'Pacific'] or hour > 12 or hour < 1 or minute > 59 or minute < 0:
    print('Invalid input')
    exit()

if start_zone == end_zone:
    print('The time is the same as the starting time zone.')
elif start_zone == 'Pacific':
    if hour == 12:
        hour = 0
    if end_zone == 'Mountain':
        if hour == 11:
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour += 1
    elif end_zone == 'Central':
        if hour >= 10:
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour += 2
    elif end_zone == 'Eastern':
        if hour >= 9:
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour += 3
    if hour > 12:
        hour -= 12
elif start_zone == 'Mountain':
    if hour == 12:
        hour = 0
    if end_zone == 'Central':
        if hour == 11:
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour += 1
    elif end_zone == 'Eastern':
        if hour >= 10:
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour += 2
    elif end_zone == 'Pacific':
        if hour == 0:
            hour = 11
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        else:
            hour -= 1
    if hour > 12:
        hour -= 12
elif start_zone == 'Central':
    if hour == 12:
        hour = 0
    if end_zone == 'Eastern':
        if hour == 11:
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour += 1
    elif end_zone == 'Mountain':
        if hour <= 1:
            hour = 12
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour -= 2
    elif end_zone == 'Pacific':
        if hour == 0:
            hour = 12
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour -= 1
    if hour > 12:
        hour -= 12
elif start_zone == 'Eastern':
    if end_zone == 'Central':
        if hour == 0:
            hour = 12
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour -= 1
    elif end_zone == 'Mountain':
        if hour <= 1:
            hour = 12
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour -= 2
    elif end_zone == 'Pacific':
        if hour <= 2:
            hour = 12
            if flag == 'am':
                flag = 'pm'
            else:
                flag = 'am'
        hour -= 3

print(f'The time in {end_zone} is {hour}:{minute}{flag}.')
