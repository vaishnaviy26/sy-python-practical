# Receipt Pattern Using Numbers

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nReceipt No.")
for i in range(1, 6):
    print("Receipt", i)