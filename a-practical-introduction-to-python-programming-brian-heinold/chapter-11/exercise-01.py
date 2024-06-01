# 1. Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a product
# name and print the corresponding price or a message if the product is not in the dictionary.

print("Note: To stop any phase, enter an empty line.\n")

product_dict = {}
product = input("Enter a product name to assign with a price: ")

while product:
    price = input("Enter the product price: ")
    while price == "":
        print("You must enter a price for the product.")
        price = input("Enter the product price: ")
    product_dict[product] = price
    product = input("Enter a product name to assign with a price: ")

product = input("Enter the product name to know the price: ")
while product:
    if product in product_dict:
        print("Price:", product_dict[product])
    else:
        print("Product not found, try again.")
    product = input("Enter the product name to know the price: ")
