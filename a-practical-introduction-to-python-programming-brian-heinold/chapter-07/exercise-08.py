# 8. Write a program that asks the user for an integer and creates a list that consists of the factors
# of that integer.
import math

integer = int(input("Please enter an integer: "))

# factorize the integer == devisors
factors = []
SQRT = math.ceil(math.sqrt(integer))
for i in range(1, SQRT + 1):
    if integer % i == 0:
        factors.append(i)
        if i != integer // i:
            factors.append(integer // i)
print(factors)
