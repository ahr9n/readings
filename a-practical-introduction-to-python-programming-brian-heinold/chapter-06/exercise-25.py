# 25. In algebraic expressions, the symbol for multiplication is often left out, as in 3x+4y or 3(x+5).
# Computers prefer those expressions to include the multiplication symbol, like 3*x+4*y or
# 3*(x+5). Write a program that asks the user for an algebraic expression and then inserts
# multiplication symbols where appropriate.

expression = input('Enter an algebraic expression: ')

new_expression = ''
for i in range(len(expression) - 1, -1, -1):
    if not expression[i].isdigit() and i + 1 < len(expression) and expression[i + 1].isalpha():
        new_expression += '*1'
    if expression[i].isdigit() or expression[i] in '+-*\\)':
        new_expression += expression[i]
    elif expression[i].isalpha():
        if expression[i - 1].isdigit():
            new_expression += expression[i] + '*'
        else:
            new_expression += expression[i]
    elif expression[i] == '(':
        if expression[i - 1].isalpha() or expression[i - 1] == ')':
            new_expression += expression[i] + '*'
        else:
            new_expression += expression[i]

new_expression = new_expression[::-1]
if new_expression[0].isalpha():
    new_expression = '1*' + new_expression
elif new_expression[0] == '*':
    new_expression = '1' + new_expression

print(new_expression)

""" manual generated tests, enough for the problem:
input: x
output: 1*x

input: 3x+9
output: 3*x+9

input: 3x(x+7y+9)(i+o)
output: 3*x*(1*x+7*y+9)*(1*i+1*o)

input: x(5+4x(x+7y+9)+(i+o)(u+9))
output: 1*x*(5+4*x*(1*x+7*y+9)+(1*i+1*o)*(1*u+9))
"""
