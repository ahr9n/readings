# Given two dates entered as strings in the format mm/dd/yyyy, where the years are between 1901 and 2099.
# Determine the number of days between the two dates, considering leap years.

first_date = input('Enter the first date in the format mm/dd/yyyy: ')
second_date = input('Enter the second date in the format mm/dd/yyyy: ')

first_month, first_day, first_year = int(first_date[:2]), int(first_date[3:5]), int(first_date[-4:])
second_month, second_day, second_year = int(second_date[:2]), int(second_date[3:5]), int(second_date[-4:])

# Another type:
# first_date_list = first_date.split('/')
# second_date_list = second_date.split('/')

# first_month = int(first_date_list[0])
# first_day = int(first_date_list[1])
# first_year = int(first_date_list[2])

# second_month = int(second_date_list[0])
# second_day = int(second_date_list[1])
# second_year = int(second_date_list[2])

# Check if the first date is before the second date, if not, swap them
comes_first = True
if first_year > second_year:  # 1999 < 2000
    comes_first = False
elif first_year == second_year:
    if first_month > second_month:  # 1/2000 < 3/2000
        comes_first = False
    elif first_month == second_month:
        if first_day > second_day:  # 1/1/2000 < 1/14/2000
            comes_first = False
        elif first_day == second_day:
            print('The two dates are the same, so there are no days between them.')
            exit()
if not comes_first:
    first_month, second_month = second_month, first_month
    first_day, second_day = second_day, first_day
    first_year, second_year = second_year, first_year

# Calculate the number of days between the two dates, considering first_date comes first
# Cases in form mm/dd/yyyy
# 1. 03/14/2010 - 05/23/2010 -> (31 - 14) + 30 + 23 - 1 = 69 days_between
# 2. 02/14/2010 - 01/23/2011 -> (28 - 14) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 23 - 1 = 342 days_between

days_between = 0
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

if first_year == second_year:                           # 2010 - 2010
    if first_month == second_month:                     # 03/14/2010 - 03/23/2010
        days_between = second_day - first_day - 1
    else:                                               # 03/14/2010 - 05/23/2010
        days_between = days[first_month] - first_day
        for month in range(first_month + 1, second_month):
            days_between += days[month]
        days_between += second_day - 1
        if first_year % 4 == 0 and first_month == 2:    # 02/14/2010 - 05/23/2010
            days_between += 1
else:
    # from first_date till the end of first_year
    days_between += days[first_month] - first_day
    if first_year % 4 == 0 and first_month < 2:        # 02/14/2010 - 05/23/2010
        days_between += 1
    for month in range(first_month + 1, 13):
        days_between += days[month]

    # years between first_year and second_year          # 2010 - 2010 or 2021
    for year in range(first_year + 1, second_year):
        days_between += 365
        if year % 4 == 0:
            days_between += 1

    # from second_year till the end of second_date
    for month in range(1, second_month):
        days_between += days[month]
    days_between += second_day - 1
    if second_year % 4 == 0 and second_month > 2:       # 02/14/2010 - 05/23/2010
        days_between += 1

print('The number of days between the two dates, excluding, is:', days_between)
