# 1. Write a program that asks the user to enter a string. The program should then print the
# following:
# (a) The total number of characters in the string
# (b) The string repeated 10 times
# (c) The first character of the string (remember that string indices start at 0)
# (d) The first three characters of the string
# (e) The last three characters of the string
# (f) The string backwards
# (g) The seventh character of the string if the string is long enough and a message otherwise
# (h) The string with its first and last characters removed
# (i) The string in all caps
# (j) The string with every 'a' replaced with an 'e'
# (k) The string with every letter replaced by a space

s = input("Enter a string: ")

print("The total number of characters in the string is:", len(s))
print("The string repeated 10 times is: '", s * 10, "'", sep="")
print("The first character of the string is: '", s[0], "'", sep="")
print("The first three characters of the string are: '", s[0:3], "'", sep="")
print("The last three characters of the string are: '", s[-3:], "'", sep="")
print("The string backwards is: '", s[::-1], "'", sep="")  # s[-1:-(len(s) + 1):-1]

if len(s) >= 7:
    print("The seventh character of the string is: '", s[6], "'", sep="")
else:
    print("Error: The string length is below seven, so no seventh character exists.")

if len(s) <= 2:
    print("The string with its first and last characters removed is: '", "'", sep="")
else:
    print(
        "The string with its first and last characters removed is: '",
        s[1 : len(s) - 1],
        "'",
        sep="",
    )

print("The string in all caps is: '", s.upper(), "'", sep="")
print(
    "The string with every 'a' replaced with an 'e' is: '",
    s.replace("a", "e"),
    "'",
    sep="",
)
print(
    "The string with every letter replaced by a space is: '", len(s) * " ", "'", sep=""
)
