myList = list()
myOtherList = [1,2,3,4]
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.insert(2,34)
myList.remove(4)
print("El valor del pop es : ", myList.pop())
print("El valor del pop es : ", myList.pop(2))
print(myList)
print(myOtherList)
print(len(myList))

thirdList = [28, 1.80, "Edivaldo", "Gomes"]
print(thirdList)
age, heigh, name, surname = thirdList
print(age)
print(thirdList[3])

for i in thirdList[-1]:
    print(i)

del myOtherList[1]
print(myOtherList)
print(myOtherList.count(2))
myNewList = myList.copy()
myList.clear()
print(myList)
print(myNewList)

myNewList.reverse()
print(myNewList)
myNewList.append(8)
myNewList.append(3)
myNewList.append(6)
myNewList.append(4)
print(myNewList)
myNewList.sort()
print(myNewList)