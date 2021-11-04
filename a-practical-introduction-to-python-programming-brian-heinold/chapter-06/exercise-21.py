# 21. An anagram of a word is a word that is created by rearranging the letters of the original.
# For instance, two anagrams of idle are deli and lied. Finding anagrams that are real words is
# beyond our reach until Chapter 12. Instead, write a program that asks the user for a string
# and returns a random anagram of the string—in other words, a random rearrangement of the
# letters of that string.

from random import sample

s = input('Enter a string: ')
print(''.join(sample(s, len(s))))

# join the string here means to join the elements of the returned list from sample()
