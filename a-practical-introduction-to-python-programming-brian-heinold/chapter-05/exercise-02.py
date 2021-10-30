# 2. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
# 4 and how many end in a 9.

cnt4, cnt9 = 0, 0
for i in range(1, 101):
    if (i ** 2) % 10 == 4:
        cnt4 += 1
    if (i ** 2) % 10 == 9:
        cnt9 += 1

print(cnt4, 'squares of the numbers from 1 to 100 end in a 4.')
print(cnt9, 'squares of the numbers from 1 to 100 end in a 9.')
