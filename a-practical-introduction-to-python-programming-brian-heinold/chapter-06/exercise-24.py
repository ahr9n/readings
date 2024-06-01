# 24. In calculus, the derivative of x^4 is 4x^3. The derivative of x^5 is 5x^4. The derivative of x^6 is
# 6x^5. This pattern continues. Write a program that asks the user for input like x^3 or x^25
# and prints the derivative. For example, if the user enters x^3, the program should print out
# 3x^2.

# input: factor * variable ** exponent
# assume: factor and exponent are integers

expression = input("Enter an expression like x^3 or x^25: ")

factor, idx = 0, 0
if expression[0].isalpha():
    factor = 1
else:
    for i in range(len(expression)):
        idx = i
        if expression[i].isalpha():
            factor = int(expression[0:i])
            break

# input: factor
if idx == len(expression) - 1 and expression[idx].isdigit():
    print("The derivative of", expression, "is 0.")
    exit()

variable = ""
for i in range(idx, len(expression)):
    idx = i
    if expression[i] == "^":
        variable = expression[idx:i]
        break

if idx == len(expression) - 1:  # input: factor * variable
    exponent = 0
else:  # input: factor * variable ** exponent
    exponent = int(expression[idx + 1 :])

if exponent == 0:
    print("The derivative of", expression, f"is {factor}.")
else:
    print(
        f"The derivative of {expression} is {factor*exponent}*{variable}^{exponent-1}"
    )
