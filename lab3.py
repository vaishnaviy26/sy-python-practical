marks =float(input("Enter your(%):"))
age=int(input("Enter your age:"))

if 17 <= age <= 25:
    if marks >=60:
        print("congratulations! You are eligible for admission.")

    else:
        print("sorry! You are Not Eligible because your marks are below 68%.")

else:
    print("sorry!You Are Not Eligible because your age is below 17 or your age is above 25.")