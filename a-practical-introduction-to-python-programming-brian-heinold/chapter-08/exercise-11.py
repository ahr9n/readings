# # 11. Section 8.3 described how to use the shuffle method to create a random anagram of a string.
# # Use the choice method to create a random anagram of a string.

import random
st = [letter for letter in 'ahmad']
anagram = ''
for i in range(len(st)):
    letter = random.choice(st)
    anagram += letter
    st.remove(letter)

print('Anagram of \'ahmad\' is:', anagram)
