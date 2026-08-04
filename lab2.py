# Simple Billing Calculator for Grocery Shop

print("===== Grocery Shop Billing Calculator =====")

# Input
item1 = float(input("Enter price of Item 1: "))
item2 = float(input("Enter price of Item 2: "))
item3 = float(input("Enter price of Item 3: "))

# Arithmetic Operator
total_bill = item1 + item2 + item3

# Discount calculation
if total_bill >= 1000:
    discount = total_bill * 0.10   # 10% discount
elif total_bill >= 500 and total_bill < 1000:
    discount = total_bill * 0.05   # 5% discount
else:
    discount = 0

# Final payable amount
final_amount = total_bill - discount

# Relational and Logical Operators Example
if total_bill >= 500 and total_bill < 1000:
    category = "Eligible for 5% Discount"
elif total_bill >= 1000:
    category = "Eligible for 10% Discount"
else:
    category = "No Discount"

# Output
print("\n===== BILL =====")
print("Total Bill      : ₹", total_bill)
print("Discount        : ₹", discount)
print("Final Amount    : ₹", final_amount)
print("Status          :", category)

print("\nThank You! Visit Again.")