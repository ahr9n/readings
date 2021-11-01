# 4. Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000

answer = 0
for i in range(1, 2001):
    if i % 2 == 0:
        answer -= i
    else:
        answer += i

print(answer)

# Can you notice a pattern? ;)
