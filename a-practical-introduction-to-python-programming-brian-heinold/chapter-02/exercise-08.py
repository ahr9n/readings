# Write a program that asks the user for their name and how many times to print it. The pro-
# gram should print out the user’s name the specified number of times.

# Enter your name: Ahmad Abdulrahman
# How many times do you need to print your name? 10

name = input("Enter your name: ")
times = eval(input("How many times do you need to print your name? "))

for i in range(times):
    print(name)
