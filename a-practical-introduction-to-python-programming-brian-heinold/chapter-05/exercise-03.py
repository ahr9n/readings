# 3. Write a program that asks the user to enter a value n, and then computes (1 + 1\2 + 1\3 + ... + 1\n) −
# ln(n). The ln function is 'log' in the 'math' module.

from math import log

n = eval(input("Enter a value: "))

answer = 0
for i in range(1, n + 1):
    answer += 1 / i
answer -= log(n)

print(answer)
