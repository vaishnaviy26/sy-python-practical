# Customer Feedback Formatter

customer_name = input("Enter Customer Name: ")
product_name = input("Enter Product Name: ")
feedback = input("Enter Customer Feedback: ")
rating = input("Enter Rating (1-5): ")


customer_name = customer_name.title()
product_name = product_name.title()
feedback = feedback.strip().capitalize()


print("\n" + "=" * 50)
print("        CUSTOMER FEEDBACK REPORT")
print("=" * 50)

print(f"Customer Name : {customer_name}")
print(f"Product Name  : {product_name}")
print(f"Rating        : {rating}/5")
print(f"Feedback      : {feedback}")

print("=" * 50)

if "good" in feedback.lower() or "excellent" in feedback.lower() or "great" in feedback.lower():
    print("Status        : Positive Feedback 😊")
elif "bad" in feedback.lower() or "poor" in feedback.lower() or "worst" in feedback.lower():
    print("Status        : Negative Feedback 😞")
else:
    print("Status        : Neutral Feedback 🙂")

print("=" * 50)