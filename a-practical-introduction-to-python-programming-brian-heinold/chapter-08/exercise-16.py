# 16. Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]. Use a list comprehension to
# produce a list of the gaps between consecutive entries in L. Then find the maximum gap size
# and the percentage of gaps that have size 2.

L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

lists = [[i for i in range(L[j] + 1, L[j + 1])] for j in range(1, len(L) - 1)]
print(lists)

gaps = [len(lists[i]) for i in range(len(lists))]
print(
    "The maximum gap is {} and the percentage of gaps that have size 2 is {}.".format(
        max(gaps), gaps.count(2) / len(gaps)
    )
)
