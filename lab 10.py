product=[]
prices=[]

while True:
    print("\n-----------product Inventory----------")
    print("1.Add product")
    print("2.Display product")
    print("3.update product")
    print("4.Delete product")
    print("5.search product")
    print("6.sort product")
    print("7.Exit")

    choice=int(input("Enter your choice:"))

    if choice == 1:
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))

        product.append(name)
        prices.append(price)
        print("Product Added successfully!")

    elif choice == 2:
        if len(product)==0:
            print("Product Not Available.")
        else:
             for i in range(len(product)):
                 print(product[i],":",prices[i])
            

