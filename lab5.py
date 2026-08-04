# Monthly Expense Tracker

print("=== Monthly Expense Tracker ===")

# Ask the user for the number of days to record expenses
days = int(input("Enter the number of days you want to record expenses: "))

total_expense = 0

# For loop to record daily expenses
for day in range(1, days + 1):
    print(f"\nDay {day}")

    daily_total = 0

    # While loop to enter multiple expenses for the day
    while True:
        expense = float(input("Enter expense amount: ₹"))
        daily_total += expense

        choice = input("Do you want to add another expense for this day? (yes/no): ").lower()

        if choice != "yes":
            break

    print(f"Total expense for Day {day}: ₹{daily_total:.2f}")

    # Accumulation logic
    total_expense += daily_total

# Display final result
print("\n===== Monthly Expense Summary =====")
print(f"Total Monthly Expense: ₹{total_expense:.2f}")