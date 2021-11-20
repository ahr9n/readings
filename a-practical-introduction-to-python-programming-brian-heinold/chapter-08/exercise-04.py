# 4.
# (a) Write a program that asks the user to enter a sentence and then randomly rearranges the
# words of the sentence. Don’t worry about getting punctuation or capitalization correct.
# (b) Do the above problem, but now make sure that the sentence starts with a capital, that
# the original first word is not capitalized if it comes in the middle of the sentence, and
# that the period is in the right place.

import random
sentence = input('Enter a sentence: ').split()  # sentence is a list of words

a = sentence
random.shuffle(a)
print(' '.join(a))

b = sentence
# remove the last character of the last word
b[-1] = b[-1][:-1]
# lowercase the list
b = [word.lower() for word in b]
# shuffle the list
random.shuffle(b)
# capitalize the first word
b[0] = b[0].capitalize()
# add the period
b[-1] = b[-1] + '.'
print(' '.join(b))
