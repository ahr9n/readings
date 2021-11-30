# 13. Let L be a list of strings. Write list comprehensions that create new lists from L for each of the
# following.
# (a) A list that consists of the strings of L with their first characters removed
# (b) A list of the lengths of the strings of L
# (c) A list that consists of only those strings of L that are at least three characters long

# probably, he meant 'L' not 's'

L = ['ahmad', 'ali', 'mohammad', 'hi']

new_list_a = [x[1:] for x in L]
print(new_list_a)

new_list_b = [len(x) for x in L]
print(new_list_b)

new_list_c = [x for x in L if len(x) >= 3]
print(new_list_c)

