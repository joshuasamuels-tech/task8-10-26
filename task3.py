def calculate_total(price, quantity):
    return price * quantity


product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = calculate_total(price, quantity)

print("\n--- Shopping Bill ---")
print("Product:", product_name)
print("Quantity:", quantity)
print("Final Amount: ₹", total)