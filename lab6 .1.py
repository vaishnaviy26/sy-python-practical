# Invoice Pattern Using Stars

rows = 8
cols = 40

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("* Item        Qty      Price        *")
print("* Rice         2       100          *")
print("* Sugar        1        50          *")
print("* Oil          3       450          *")

for i in range(cols):
    print("*", end="")