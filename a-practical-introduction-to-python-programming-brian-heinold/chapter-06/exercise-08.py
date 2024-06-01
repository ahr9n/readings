# 8. At a certain school, student email addresses end with @student.college.edu, while pro-
# fessor email addresses end with @prof.college.edu. Write a program that first asks the
# user how many email addresses they will be entering, and then has the user enter those ad-
# dresses. After all the email addresses are entered, the program should print out a message
# indicating either that all the addresses are student addresses or that there were some profes-
# sor addresses entered.

times = eval(input("How many addresses do you want to enter? "))

error, all_student = False, True
for i in range(times):
    print("Enter the #", i + 1, " address: ", sep="", end="")
    s = input()

    # idx = s.index('@') # returns an exception if false
    idx = s.find("@")

    if idx <= 0:
        error = True
    else:
        mail = s[idx:]
        if mail == "@prof.college.edu":
            all_student = False
        elif mail != "@student.college.edu":
            error = True

if error:
    print("Error: Invalid input.")
elif all_student:
    print("All the addresses are student addresses.")
else:
    print("There were some professor addresses entered.")
