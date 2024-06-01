# 8. Write a program that asks the user for a number of seconds and prints out how many minutes
# and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
# operator to get minutes and the % operator to get seconds.]

seconds = eval(input("Enter a number of seconds: "))

minutes = seconds // 60
seconds %= 60

print("That means", minutes, "minutes and", seconds, "seconds.")
