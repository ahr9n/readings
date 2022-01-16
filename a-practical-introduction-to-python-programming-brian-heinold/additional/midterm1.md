<h1 align="center">Midterm Exam (1)</h1>

**1.Write a Python program that:
a) Read a list of students' grades of some course out of 100.
b) The program then translates numeric grades into rate of appreciation (Excellent, Very Good, etc.).
c) The program calculates and stores the frequencies of rate of appreciations into a Python dictionary.
d) The content of the dictionary are then printed in a tabular form.**

**Answer:**

```python
grades = input('Enter grades out of 100: ').split()

rates = []
for grade in grades:
    if 85 <= int(grade) <= 100:
        rates.append('Excellent')
    elif 75 <= int(grade):
        rates.append('Very Good')
    elif 65 <= int(grade):
        rates.append('Good')
    elif 50 <= int(grade):
        rates.append('Pass')
    else:
        rates.append('Fail')

frequency = {}
for rate in rates:
    if rate in frequency:
        frequency[rate] += 1
    else:
        frequency[rate] = 1
        
print('\nFrequency of grades:')
for key, value in frequency.items():
    print(key, ':', value)
```

---

**2. Given two dates entered as strings in the format mm/dd/yyyy, where the years are between 1901 and 2099.
Determine the number of days between the two dates, considering leap years.**

**Answer:** This should be BASED ON inclusion-exclusion principle.

```python
first_date = input('Enter the first date in the format mm/dd/yyyy: ')
second_date = input('Enter the second date in the format mm/dd/yyyy: ')

first_month, first_day, first_year = int(first_date[:2]), int(first_date[3:5]), int(first_date[-4:])
second_month, second_day, second_year = int(second_date[:2]), int(second_date[3:5]), int(second_date[-4:])

# Another type (using lists):
# first_date_list, second_date_list = first_date.split('/'), second_date.split('/')
# first_month, first_day, first_year = int(first_date_list[0]), int(first_date_list[1]). int(first_date_list[2])
# second_month, second_day, second_year = int(second_date_list[0]), int(second_date_list[1]), int(second_date_list[2])

# In a complete solution, you must check first if the first_date is before second_date, if not; to swap them (validation step).
# Otherwise, you may assume it is always true that first_date is before second_date (ask for a clarification).

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

# Now, calculate the number of days between the two dates, considering first_date is the first:

days_between = 0
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Cases in form 'mm/dd/yyyy'
# 03/14/2010 - 05/23/2010 -> (31 - 14) + 30 + 23 - 1 = 69 days_between

years = first_year - second_year
months = first_month - second_month

if years == 0:
    if months == 0:
        days_between = first_day - second_day
    else:                                               # Same year, but different months
        days_between = days[first_month] - first_day
        if first_year % 4 == 0 and first_month <= 2:    # 02/14/2010 - 05/23/2010
            days_between += 1
        for month in range(first_month + 1, second_month):
            days_between += days[month]
        days_between += second_day - 1
    print('The number of days between the two dates, excluding, is:', days_between)
    exit()
    
# 02/14/2010 - 01/23/2011 -> (28 - 14) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 23 - 1 = 342 days_between

# It is always that years > 0, so get days from first_date till the end of first_year
days_between = days[first_month] - first_day
if first_year % 4 == 0 and first_month <= 2:            # 02/14/2010 - 05/23/2011
    days_between += 1
for month in range(first_month + 1, 13):
    days_between += days[month]

# get years between first_year and second_year          # 2010 - [2010 or 2021]
for year in range(first_year + 1, second_year):
    days_between += 365
    if year % 4 == 0:
        days_between += 1

# get days from second_year till the end of second_date
for month in range(1, second_month):
    days_between += days[month]
if second_year % 4 == 0 and second_month > 2:           # 02/14/2010 - 05/23/2010
    days_between += 1
days_between += second_day - 1

print('The number of days between the two dates, excluding, is:', days_between)
# End of program
```
```python
# Another solution using 'datetime' module:

from datetime import date

d0 = date(first_year, first_month, first_day)
d1 = date(second_year, second_month, second_day)

# using 'abs' saves your mind from considering a lot of IFFs as mentioned before
delta = abs(d1 - d0)

print('The number of days between the two dates, excluding, is:', delta.days - 1)
```
