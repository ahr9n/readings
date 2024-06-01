# 4. Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
# entries in the list that are greater than 10 with 10.

L = input("Enter a list of numbers between 1 and 12: ")
L = L.split()

for i in range(len(L)):
    L[i] = int(L[i])
    if L[i] > 10:
        L[i] = 10

# L = [int(i) if int(i) <= 10 else 10 for i in L]
# List comprehensions (next chapter)

print(L)
