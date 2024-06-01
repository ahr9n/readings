# 2. Using the dictionary created in the previous problem, allow the user to enter a dollar amount
# and print out all the products whose price is less than that amount.

print("To stop any phase, enter an empty product name.")

product_dict = {}
while True:
    product = input("Enter a product name to assign with a price: ")
    if product == "":
        break
    price = input("Enter the product price: ")
    while price == "":
        print("You must enter a price for the product.")
        price = input("Enter the product price: ")
    product_dict[product] = price

amount = input("Enter an amount to check against: ")
for product, price in product_dict.items():
    if float(price) < float(amount):
        print(f"{product} costs ${price}")
