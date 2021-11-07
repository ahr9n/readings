# 13. Write a program that removes any repeated items from a list so that each item appears at most
# once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

L = [1, 3, 2, 3, 4, 1, 0, 5]

L.sort()
new_list = [L[0]]
for i in range(1, len(L)):
    # if L[i] not in new_list:  # not efficient
    #     new_list.append(L[i])

    if L[i] != L[i - 1]:  # efficient, and this is why we sort the list first
        new_list.append(L[i])

print(new_list)
