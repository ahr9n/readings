# 17. Write a program that generates the 26-line block of letters partially shown below. Use a loop
# containing one or two print statements.
# abcdefghijklmnopqrstuvwxyz
# bcdefghijklmnopqrstuvwxyza
# cdefghijklmnopqrstuvwxyzab
# ...
# yzabcdefghijklmnopqrstuvwx
# zabcdefghijklmnopqrstuvwxy

line = "abcdefghijklmnopqrstuvwxyz"
for j in range(1, 27):
    print(line)
    # create a variable for the string
    new_string = ""
    # loop through the string
    for i in range(len(line) - 1):
        # add the next letter to the new string
        new_string += line[i + 1]
    # add the first letter to the new string
    new_string += line[0]
    # return the new string
    line = new_string

    # the above code is the same as a rotate function :)
    # made by github-copilot :)
