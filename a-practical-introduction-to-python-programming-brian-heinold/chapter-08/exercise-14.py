# 14. Use a list comprehension to produce a list that consists of all palindromic numbers between
# 100 and 1000.

L = [x for x in range(100, 1000) if str(x) == str(x)[::-1]]
print(L)

# notice that the above is not the same as the following
# M = [x if str(x) == str(x)[::-1] else '' for x in range(100, 1000)]
# print(M)
