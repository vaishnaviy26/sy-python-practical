list=[1,2,3,4,5,6,7,8]
print(list)

print(list[0])

list[0]=10
print(list)

list.append(3)
print(list)

list.insert(5,15)
print(list)

list.extend([20,21,22,23])
print (list)

list.remove(5)
print(list)

list.pop(7)
print(list)

del list[4]
print(list)

print(len(list))

if 1 in list:
    print("Element is present")
else:
    print("Element is absent")



for i in list:
    print(i)



print(list.count(3))


print(list.index(6))

list.reverse()
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

newlist=list.copy()
print(newlist)

list.clear()
print(list)
