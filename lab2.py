print("===== Grocery Shop Billing Calculator =====")

item1 = float(input("Enter price of Item 1: "))
item2 = float(input("Enter price of Item 2: "))
item3 = float(input("Enter price of Item 3: "))

total_bill = item1 + item2 + item3

if total_bill >= 1000:
    discount = total_bill * 0.10   
elif total_bill >= 500 and total_bill < 1000:
    discount = total_bill * 0.05
else:
    discount = 0

final_amount = total_bill - discount

if total_bill >= 500 and total_bill < 1000:
    category = "Eligible for 5% Discount"
elif total_bill >= 1000:
    category = "Eligible for 10% Discount"
else:
    category = "No Discount"

print("\n===== BILL =====")
print("Total Bill      : ₹", total_bill)
print("Discount        : ₹", discount)
print("Final Amount    : ₹", final_amount)
print("Status          :", category)

print("\nThank You! Visit Again.")
