
# Start item count 0
total = 0
number_of_item = int(input("Enter number of items: "))
# loop until positive value received
while number_of_item < 0:
    print("Invalid Entry")
    number_of_item = int(input("Enter number of items: "))
# loop for number_of_items
for i in range(number_of_item):
    price = float(input("Price of item:$ "))
# add price value to total variable
    total += price
# Apply discount when over $100
if total > 100:
    total *= 0.9
    print("10% discount applied")
print("Number of items:", number_of_item, "Total Cost: $", total)
