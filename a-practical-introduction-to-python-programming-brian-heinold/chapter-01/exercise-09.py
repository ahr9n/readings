# A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
# the percent tip they want to leave. Then print both the tip amount and the total bill with the
# tip included

# Enter the price of the meal: 75
# Enter the percent tip: 1/5

meal_price = eval(input('Enter the price of the meal: '))
percent_tip = eval(input('Enter the percent tip: '))

tip_amount = meal_price * percent_tip
total_bill_including_tip = meal_price + tip_amount

print('The tip amount is:', tip_amount)  # output: 15.0
print('The total bill with the tip included is:', total_bill_including_tip)  # output: 90.0

# Rules:
# Variable names cannot contain spaces.
# Variable names can contain letters, numbers, and the underscore.
