# 11. Write a program that asks the user to enter a weight in kilograms. The program should
# convert it to pounds, printing the answer rounded to the nearest tenth of a pound.

kilograms = eval(input('Enter a weight in kilograms: '))

pounds = kilograms * 2.20462262185
pounds = round(pounds, 1)

print('Weight in pounds rounded to the nearest tenth of pound:', pounds)
