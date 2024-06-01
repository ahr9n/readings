# The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
# number thereafter is the sum of the two preceding numbers. Write a program that asks the
# user how many Fibonacci numbers to print and then prints that many.
#                   1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...

# How many Fibonacci numbers to print? 10

times = eval(input("How many Fibonacci numbers to print? "))

first = 1
second = 1

if times <= 2:
    print(first)
    if times == 2:
        print(second)
else:
    print(first)
    print(second)
    for i in range(2, times):
        now = first + second
        print(now)
        first = second
        second = now

# To handle the case if input <= 2, you should use 'if conditions' or 'lists'
