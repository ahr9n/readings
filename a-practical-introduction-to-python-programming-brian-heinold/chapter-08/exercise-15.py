# 15. Use a list comprehension to create the list below, which consists of ones separated by increas-
# ingly many zeroes. The last two ones in the list should be separated by ten zeroes.
# [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

helper = [[0] * i + [1] for i in range(11)]
L = [elem for List in helper for elem in List]
print(L)
