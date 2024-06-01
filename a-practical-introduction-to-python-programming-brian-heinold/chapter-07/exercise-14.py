# 14. Write a program that asks the user to enter a length in feet. The program should then give
# the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
# meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
# enter a 2, then the program converts to yards, etc. While this can be done with if statements,
# it is much shorter with lists and it is also easier to add new conversions if you use lists.

feet = eval(input("Enter a length in feet: "))
options = [
    "inches",
    "yards",
    "miles",
    "millimeters",
    "centimeters",
    "meters",
    "kilometers",
]
convert_factor = [12, 1 / 3, 1 / 5280, 304.8, 30.48, 0.3048, 1 / 3280.84]

print("Choose a unit to convert to: ")  # display options
for i in range(len(options)):
    print(f"Enter {i+1} for {options[i]}")

convert = eval(input("Enter a number: "))
if convert > 7 or convert < 1:
    print("Invalid choice")
else:
    print(f"{feet} feet is {feet * convert_factor[convert-1]} {options[convert-1]}")

# if convert == 1:
#     inches = feet * 12
#     print(f'{feet} feet is {inches} inches')
# elif convert == 2:
#     yards = feet / 3
#     print(f'{feet} feet is {yards} yards')
# elif convert == 3:
#     miles = feet / 5280
#     print(f'{feet} feet is {miles} miles')
# elif convert == 4:
#     millimeters = feet * 304.8
#     print(f'{feet} feet is {millimeters} millimeters')
# elif convert == 5:
#     centimeters = feet * 30.48
#     print(f'{feet} feet is {centimeters} centimeters')
# elif convert == 6:
#     meters = feet * 0.3048
#     print(f'{feet} feet is {meters} meters')
# elif convert == 7:
#     kilometers = feet / 3280.84
#     print(f'{feet} feet is {kilometers} kilometers')
# else:
#     print('Invalid entry')
