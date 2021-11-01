# 10. Ask the user to enter 10 test scores. Write a program to do the following:
# (a) Print out the highest and lowest scores.
# (b) Print out the average of the scores.
# (c) Print out the second largest score.
# (d) If any of the scores is greater than 100, then after all the scores have been entered, print
# a message warning the user that a value over 100 has been entered.
# (e) Drop the two lowest scores and print out the average of the rest of them.

first = eval(input('Enter the #1 test score: '))
second = eval(input('Enter the #2 test score: '))
third = eval(input('Enter the #3 test score: '))
fourth = eval(input('Enter the #4 test score: '))

average = first + second + third + fourth
highest1 = max(max(first, second), max(third, fourth))
lowest1 = min(min(first, second), min(third, fourth))
highest2, lowest2 = 0, 0

if first == highest1:
    highest2 = max(second, max(third, fourth))
elif second == highest1:
    highest2 = max(first, max(third, fourth))
elif third == highest1:
    highest2 = max(first, max(second, fourth))
elif fourth == highest1:
    highest2 = max(first, max(third, second))

if first == lowest1:
    lowest2 = min(second, min(third, fourth))
elif second == lowest1:
    lowest2 = min(first, min(third, fourth))
elif third == lowest1:
    lowest2 = min(first, min(second, fourth))
elif fourth == lowest1:
    lowest2 = min(first, min(third, second))

for i in range(5, 11):
    print('Enter the #', i, ' test score: ', sep='', end='')
    now = eval(input())
    average += now

    if highest1 < now:
        highest2 = highest1
        highest1 = now
    elif highest1 == now:
        highest2 = highest1

    if lowest1 > now:
        lowest2 = lowest1
        lowest1 = now
    elif lowest1 == now:
        lowest2 = lowest1

average /= 10

if highest1 > 100:
    print('Warning: A value over 100 has been entered!')

print('The highest test score is:', highest1)
print('The lowest test score is:', lowest1)
print('The average of test scores is:', average)
print('The second highest score is:', highest2)

average *= 10
average -= lowest1 + lowest2
average /= 8
print('After dropping the two lowest scores, the average of the rest is:', average)
