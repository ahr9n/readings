# 8. Write a program that simulates drawing names out of a hat. In this drawing, the number of
# hat entries each person gets may vary. Allow the user to input a list of names and a list of
# how many entries each person has in the drawing, and print out who wins the drawing.

# this is what copilot understood, and I have no idea what I'm doing :/

# Initialize variables
names = []
# Get the names
while True:
    name = input("Enter a name (or press enter to finish): ")
    if name == "":
        break
    names.append(name)

# Initialize variables
entries = []
# Get the entries
while True:
    entry = eval(input("Enter the number of entries (or press enter to finish): "))
    if entry == "":
        break
    entries.append(entry)

# Initialize variables
winner = ""
# Get the winner, the name with the most entries
winner = names[0]
for i in range(len(names) - 1):
    if entries[i] > entries[i + 1]:
        winner = names[i]

print("The winner is: " + winner)
