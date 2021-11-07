# 10. Write a program that rotates the elements of a list so that the element at the first index moves
# to the second index, the element in the second index moves to the third index, etc., and the
# element in the last index moves to the first index.

L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    print(L)
    L = L[1:] + L[:1]
