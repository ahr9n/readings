# 1. Write a program that asks the user to enter a list of integers. Do the following:
# (a) Print the total number of items in the list.
# (b) Print the last item in the list.
# (c) Print the list in reverse order.
# (d) Print Yes if the list contains a 5 and No otherwise.
# (e) Print the number of fives in the list.
# (f) Remove the first and last items from the list, sort the remaining items, and print the resut.
# (g) Print how many integers in the list are less than 5.


list_of_numbers = input('Enter a list of numbers: ')

list_of_numbers = list_of_numbers.split()
# explained in next chapter, but necessary to do it here

print('The total number of items in the list is:', len(list_of_numbers))
print('The last item in the list is:', list_of_numbers[-1])
print('The list in reverse order is:', list_of_numbers[::-1])
if '5' in list_of_numbers:
    print('Yes')
else:
    print('No')
print('The number of fives in the list is:', list_of_numbers.count('5'))
list_of_numbers.remove(list_of_numbers[0])
list_of_numbers.remove(list_of_numbers[-1])
list_of_numbers.sort()
print('The list with the first and last items removed and sorted is:', list_of_numbers)

less_than_5 = 0
for i in list_of_numbers:
    if int(i) < 5:
        less_than_5 += 1
print('The number of integers in the list are less than 5 is:', less_than_5)
