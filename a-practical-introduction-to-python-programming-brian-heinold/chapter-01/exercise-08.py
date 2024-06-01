# Write a program that asks the user to enter three numbers (use three separate input state-
# ments). Create variables called total and average that hold the sum and average of the
# three numbers and print out the values of total and average.

# Enter the first number: 7
# Enter the second number: 5
# Enter the third number: 3

first = eval(input("Enter the first number: "))
second = eval(input("Enter the second number: "))
third = eval(input("Enter the third number: "))

total = first + second + third
average = (first + second + third) / 3

print("Total of numbers is:", total)  # output: 15
print("Average of numbers is:", average)  # output: 5.0
