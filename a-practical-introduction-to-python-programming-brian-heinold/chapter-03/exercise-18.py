# 18. Write a program that given an amount of change less than $1.00 will print out exactly how
# many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.
# [Hint: the // operator may be useful.]

change = eval(input('Enter an amount of change less than $1.00 in cents: '))

# Hands on money :)
# https://www.nbp.org/ic/nbp/programs/gep/lemon/lemon-money.html
# Penny = 1 cent
# Nickel = 5 cents
# Dime = 10 cents
# Quarter = 25 cents

quarter = change // 25
change %= 25
dime = change // 10
change %= 10
nickel = change // 5
change %= 5
penny = change

print('The needed money to efficiently make that change:')
print(quarter, 'quarters,', dime, 'dimes,', nickel, 'nickels and', penny, 'pennies.')
