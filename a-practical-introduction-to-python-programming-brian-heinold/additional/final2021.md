<h1 align="center">Final Exam 20/21</h1>

**Question 1:** Students' data is stored in a text file named "students.txt". Separated by commas, each student record
contains the student ID, student name, then student numeric grade. Write a Python program to do the following:
a) Read the data from a text file named "students.txt". b) Split students' records into lines and store them as a list
of strings. c) Build a list of lists to simulate a two-dimensional array. In each row of the array, index zero will
contain student ID, index one will contain student name, index two will contain student numeric grade, index three will
contain student rate (Excellent, Very Good, Good, Pass, or Fail).
(N.B. Your program is supposed to calculate the student rate of appreciation due to university rules.)
d) Create a Python dictionary to calculate the frequency of each rate of appreciation of the students, then print this
dictionary in a tabular form.

**Answer:**

```python
data = open('students.txt').read()

data = data.split('\n')


def rate(grade):
    if 85 <= grade <= 100:
        return 'Excellent'
    elif 75 <= grade <= 84:
        return 'Very Good'
    elif 65 <= grade <= 74:
        return 'Good'
    elif 50 <= grade <= 64:
        return 'Pass'
    elif 0 <= grade <= 49:
        return 'Fail'
    else:
        return 'Invalid input'


students = [[] for i in range(len(data))]
for i in range(len(students)):
    students[i] = data[i].split(',')
    students[i].append(rate(int(students[i][2])))

frequency = {}
for i in range(len(students)):
    if students[i][3] in frequency:
        frequency[students[i][3]] += 1
    else:
        frequency[students[i][3]] = 1
print('Frequency of each rate of appreciation of the students:')
for key, value in frequency.items():
    print(key, ': ', value, sep='')

# End of program
```

---

**Question 2:** One way to encrypt a message is to rearrange the characters. TO encrypt a string message, your algorithm
will pick out the characters at even indices, put them first in the encrypted string, and follow them by the characters
at odd indices. Write a program that asks the user to enter a string and use this method to encrypt the string. Your
program must contain two different functions for encryption and decryption.

**Answer:**

```python
message = input('Enter a string: ')


def encrypt(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 == 0]
                   + [s[i] for i in range(len(s)) if i % 2 == 1])


def decrypt(s):
    if len(s) % 2 == 0:
        first = s[:len(s) // 2]  # first half of the string
        second = s[len(s) // 2:]  # second half of the string
    else:  # we put even indices first, so the length of first half = ceil(len(s)/2.0) 
        first = s[:len(s) // 2 + 1]
        second = s[len(s) // 2 + 1:]

    ret = ''.join([first[i] + second[i] for i in range(len(second))])
    if len(ret) % 2 != 0:  # add the last even index
        ret += first[-1]
    return ret


encrypted = encrypt(message)
print('The encrypted string is:', encrypted)

decrypted = decrypt(encrypted)
print('The decrypted string is:', decrypted)

# End of program
```

_*See a simple
version: [`chapter-06/exercise-22.py`](https://github.com/ahr9n/readings/blob/main/a-practical-introduction-to-python-programming-brian-heinold/chapter-06/exercise-22.py)
._

---

**Question 3:** _Same as question 2
in [midterm2.md](https://github.com/ahr9n/readings/blob/main/a-practical-introduction-to-python-programming-brian-heinold/additional/midterm2.md)
._

---

**Question 4:** _Same
as [`gui/exercise-03.py`](https://github.com/ahr9n/readings/blob/main/a-practical-introduction-to-python-programming-brian-heinold/additional/gui/exercise-03.py)
._