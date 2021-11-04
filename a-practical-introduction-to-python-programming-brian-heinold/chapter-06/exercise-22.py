# 22. A simple way of encrypting a message is to rearrange its characters. One way to rearrange the
# characters is to pick out the characters at even indices, put them first in the encrypted string,
# and follow them by the odd characters. For example, the string 'message' would be encrypted
# as 'msaeesg' because the even characters are m, s, a, e (at indices 0, 2, 4, and 6) and the odd
# characters are e, s, g (at indices 1, 3, and 5).
# (a) Write a program that asks the user for a string and uses this method to encrypt the string.
# (b) Write a program that decrypts a string that was encrypted with this method.

s = input('Enter a string: ')

even, odd = '', ''  # initialization
for i in range(0, len(s)):
    if i % 2 == 0:
        even += s[i]
    else:
        odd += s[i]
encrypted = even + odd
print('The encrypted string is:', encrypted)

decrypted, even_idx, odd_idx = '', 0, 0
for i in range(len(encrypted)):
    if i % 2 == 0:
        decrypted += even[even_idx]
        even_idx += 1
    else:
        decrypted += odd[odd_idx]
        odd_idx += 1
print('The decrypted string is:', decrypted)
