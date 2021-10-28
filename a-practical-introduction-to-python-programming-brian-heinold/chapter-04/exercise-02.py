# 2. Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temper-
# ature is in. Your program should convert the temperature to the other unit. The conversions
# are F = 9 * C / 5 + 32 and C = 5 * (F − 32) / 9.

temperature = eval(input('Enter a temperature: '))
choice = eval(input('What units, Celsius or Fahrenheit, the temperature is in? Enter \'1\' for Celsius, otherwise enter \'2\', without quotes: '))

if choice == 1:
    C = temperature
    F = 9 * C / 5 + 32
    print('Temperature in Fahrenheit is:', F)
elif choice == 2:
    F = temperature
    C = 5 * (F - 32) / 9
    print('Temperature in Celsius is:', C)

# else:
#     print('Wrong choice, try again.')
# I could add the 2 lines above if needed.
