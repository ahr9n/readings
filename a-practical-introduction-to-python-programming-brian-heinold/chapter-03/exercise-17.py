# 17. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
# determine how many leap years there have been between 1600 and that year.

year1 = 1600
year2 = eval(input("Enter a year: "))

# Assuming year2 is always after year1, so:
if year1 >= year2:
    year1, year2 = year2, year1  # swapping

# Now, I will apply inclusion-exclusion principle
# For more info: https://cp-algorithms.com/combinatorics/inclusion-exclusion.html

year1_div4 = year1 // 4
year1_div100 = year1 // 100
year1_div400 = year1 // 400

year1_leaps = year1_div4  # A year is a leap year if it is divisible by 4
year1_leaps = (
    year1_leaps - year1_div100
)  # except that years divisible by 100 are not leap years
year1_leaps = year1_leaps + year1_div400  # unless they are also divisible by 400

year2_div4 = year2 // 4
year2_div100 = year2 // 100
year2_div400 = year2 // 400
year2_leaps = year2_div4 - year2_div100 + year2_div400

print(year2_leaps - year1_leaps + 1)  # including 'year 1600' and 'year of user'

# I could make a brute-force solution, but it will fail for LARGE numbers
# leaps = 0
# for year in range(1600, year2 + 1):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         leaps += 1
# print(leaps)

# Time Complexity in inc-exc solution is nearly O(1), yet in brute-force is O(n) ;)
