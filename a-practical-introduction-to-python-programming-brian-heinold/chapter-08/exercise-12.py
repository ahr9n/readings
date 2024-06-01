# 12. Write a program that gets a string from the user containing a potential telephone number.
# The program should print 'Valid' if it decides the phone number is a real phone number, and
# 'Invalid' otherwise. A phone number is considered valid as long as it is written in the form
# abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number should contain
# only numbers and dashes, and the number of digits in each group must be correct. Test your
# program with the output shown below.
# Enter a phone number: 1-301-447-5820
# Valid
# Enter a phone number: 301-447-5820
# Valid
# Enter a phone number: 301-4477-5820
# Invalid
# Enter a phone number: 3X1-447-5820
# Invalid
# Enter a phone number: 3014475820
# Invalid

while True:
    phone_number = input("Enter a phone number: ")
    phone_number = phone_number.replace(" ", "")

    if len(phone_number) == 12:
        digits = 0
        for i in range(len(phone_number)):
            if phone_number[i].isdigit():
                digits += 1

        good_dashs = True
        if phone_number[3] != "-" or phone_number[7] != "-":
            good_dashs = False

        if digits == 10 and good_dashs:
            print("Valid")
        else:
            print("Invalid")
    elif len(phone_number) == 14 and phone_number[0] == "1":
        digits = 0
        for i in range(len(phone_number)):
            if phone_number[i].isdigit():
                digits += 1

        good_dashs = True
        if phone_number[1] != "-" or phone_number[5] != "-" or phone_number[9] != "-":
            good_dashs = False

        if digits == 11 and good_dashs:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
