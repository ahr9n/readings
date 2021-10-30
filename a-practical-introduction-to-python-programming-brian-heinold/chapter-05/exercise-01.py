# 1. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.

cnt = 0
for i in range(1, 101):
    if (i ** 2) % 10 == 1:
        cnt += 1

print(cnt)
