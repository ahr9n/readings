<h1 align="center">Midterm Exam (2)</h1>

**Question 1:** Write a program that repeatedly asks the user to enter product names and prices. Store all of these in a
dictionary whose keys are the product names and whose values are the prices. When the user is done entering products and
prices, allow them to repeatedly enter a product name and print the corresponding price or a message if the product is
not in the dictionary.

**Answer:**
See [`chapter-11/exercise-01.py`](https://github.com/ahr9n/awesome-reading/blob/main/a-practical-introduction-to-python-programming-brian-heinold/chapter-11/exercise-01.py)

_*For the sake of simplicity, you also could ask user for entering number of products._

---

**Question 2:** Write a Python program that uses a class called DATE, a class called Todays_date, and a class called
Persons_Birth_Date. The class DATE would be the parent class for the other two classes and should include fields namely:
day, month, and year. The user will be allowed to enter the date of today and his birth date, and the program would use
a function called Calculate_Age() to calculate and print the age of the user in a suitable format.**

**Answer:**

```python
class DATE:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


class Todays_date(DATE):
    def __init__(self, day, month, year):
        # to call the parent class constructor
        super().__init__(day, month, year)


class Persons_Birth_Date(DATE):
    def __init__(self, day, month, year):
        super().__init__(day, month, year)


def Calculate_Age(birth, today):
    # assuming the birth date is earlier than today
    years = today.year - birth.year
    if years == 0:
        months = today.month - birth.month
        if months == 0:
            days = today.day - birth.day
        else:
            # same year, but different months
            # assuming all months have 30 days
            days = 30 - birth.day + today.day
            months -= 1
    else:
        # months till end of birth year plus month from start of today's year till today's month
        months = 12 - birth.month + today.month
        years -= 1  # I took one year off, because I add it to months
        days = 30 - birth.day + today.day
        months -= 1  # I took one month off, because I add it to days
    return [years, months, days]


birth_date = input('Enter your birth date (dd/mm/yyyy): ').split('/')
today_date = input('Enter today\'s date (dd/mm/yyyy): ').split('/')

birth = Persons_Birth_Date(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))
today = Todays_date(int(today_date[0]), int(today_date[1]), int(today_date[2]))

age = Calculate_Age(birth, today)

print(f'Today, you have lived {age[0]} years, {age[1]} months, and {age[2]} days.')
# End of program
```

_*See the second question
in [midterm1.md](https://github.com/ahr9n/awesome-reading/blob/main/a-practical-introduction-to-python-programming-brian-heinold/additional/midterm1.md)
for more details._