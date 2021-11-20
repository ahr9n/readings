# 3.
# (a) Ask the user to enter a sentence and print out the third word of the sentence.
# (b) Ask the user to enter a sentence and print out every third word of the sentence.

sentence = input('Enter a sentence: ').split()
print('The third word of the sentence is:', sentence[2])

every_third = [sentence[i] for i in range(0, len(sentence), 3)]
print('Every third word of the sentence is:', every_third)
