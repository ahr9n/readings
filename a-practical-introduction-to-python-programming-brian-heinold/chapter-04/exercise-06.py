# 6. A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
# items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
# program that asks the user how many items they are buying and prints the total cost.

items = eval(input('How many items are you buying? '))

if items < 10:
    print('The total cost is $', items * 12, '.', sep='')
elif 10 <= items <= 99:
    print('The total cost is $', items * 10, '.', sep='')
elif items >= 100:
    print('The total cost is $', items * 7, '.', sep='')
