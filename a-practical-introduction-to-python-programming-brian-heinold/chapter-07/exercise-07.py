# 7. Write a program that takes any two lists L and M of the same size and adds their elements
# together to form a new list N whose elements are sums of the corresponding elements in L
# and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].

L = input("Enter a list of numbers: ").split()
M = input("Enter another list of numbers: ").split()

N = []
for i in range(len(L)):
    N.append(int(L[i]) + int(M[i]))
# N = [(int(L[i]) + int(M[i])) for i in range(len(L))]

print(N)
