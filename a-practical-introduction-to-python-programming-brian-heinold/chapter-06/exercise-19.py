# 19. Write a program that asks the user for a large integer and inserts commas into it according
# to the standard American convention for commas in large numbers. For instance, if the user
# enters 1000000, the output should be 1,000,000.

large_int = input('Enter a large integer: ')

large_int = large_int[::-1]
new_int = ''
for i in range(len(large_int)):
    if i % 3 == 0 and i != 0:
        new_int += ','
    new_int += large_int[i]
new_int = new_int[::-1]

print(new_int)
