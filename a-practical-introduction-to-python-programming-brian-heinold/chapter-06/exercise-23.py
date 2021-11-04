# 23. A more general version of the above technique is the rail-fence cipher, where instead of break-
# ing things into evens and odds, they are broken up by threes, fours or something larger. For
# instance, in the case of threes, the string 'secret message' would be broken into three groups. The
# first group is sr sg, the characters at indices 0, 3, 6, 9 and 12. The second group is 'eemse', the
# characters at indices 1, 4, 7, 10, and 13. The last group is 'ctea', the characters at indices 2, 5, 8,
# and 11. The encrypted message is 'sr sgeemsectea'.

# (a) Write a program the asks the user for a string and uses the rail-fence cipher in the threes
# case to encrypt the string.
# (b) Write a decryption program for the threes case.
# (c) Write a program that asks the user for a string, and an integer determining whether to
# break things up by threes, fours, or whatever. Encrypt the string using the rail-fence
# cipher.
# (d) Write a decryption program for the general case.

s = input('Enter a string: ')
# rail-fence cipher in the threes case:
one, two, three = '', '', ''  # initialization
for i in range(0, len(s), 3):
    one += s[i]
for i in range(1, len(s), 3):
    two += s[i]
for i in range(2, len(s), 3):
    three += s[i]
encrypted = one + two + three
print('The encrypted string is:', encrypted)

# decryption program for the threes case
decrypted, one_idx, two_idx, three_idx = '', 0, 0, 0
for i in range(len(s)):
    if i % 3 == 0:
        decrypted += one[one_idx]
        one_idx += 1
    elif i % 3 == 1:
        decrypted += two[two_idx]
        two_idx += 1
    else:
        decrypted += three[three_idx]
        three_idx += 1
print('The decrypted string is:', decrypted)

# manual encryption
s = input('Enter a string: ')
rail = eval(input('Enter an integer, to break things up in it: '))
encrypted = ''
for i in range(rail):
    for j in range(i, len(s), rail):
        encrypted += s[j]
print(f'The encrypted string in {rail}\'s is:', encrypted)

# decrypt rail-fence cipher

list, lst, list_idx = [], 0, []
for i in range(rail):
    list.append([])
    for j in range(i, len(s), rail):
        list[lst].append(s[j])
    list_idx.append(0)
    lst += 1

decrypted = ''
for i in range(len(s)):
    for j in range(rail):
        if i % rail == j:
            decrypted += list[j][list_idx[j]]
            list_idx[j] += 1
print('The decrypted string is:', decrypted)

# too much unnecessary effort, if I want to do it manually, list is enough :)
