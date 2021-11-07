# 3. Start with the list [8,9,10]. Do the following:
# (a) Set the second entry (index 1) to 17
# (b) Add 4, 5, and 6 to the end of the list
# (c) Remove the first entry from the list
# (d) Sort the list
# (e) Double the list
# (f) Insert 25 at index 3
# The final list should equal [4,5,6,25,10,17,4,5,6,10,17]

L = [8, 9, 10]
L[1] = 17  # replacing

L[3:3] = [4, 5, 6]  # this is adding
# insert() adds only one item to the list at the specified position

del L[0]  # deleting
# L[0:1] = []  # another shape, with same complexity o(n*k) ;)

L.sort()
L = L * 2
L.insert(3, 25)  # complexity o(n)

print(L)
