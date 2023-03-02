mySet = set()
myOtherSet = {}
print(type(mySet))
print(type(myOtherSet))

mySet.add(12)
myOtherSet = {12, "Azul", "Rojo", 23}
print(type(myOtherSet))
print(mySet)
print(len(myOtherSet))
#print(myOtherSet[2]) # TypeError: 'set' object is not subscriptable

myOtherSet.add(6) # u set no permite duplicidad de valores
myOtherSet.add(6)
print(myOtherSet)# Un set no es una extructura ordenada
myOtherSet.remove(12)
print(myOtherSet)

print("Azul" in myOtherSet)
print("Azule" in myOtherSet)
mySet.clear()
print(mySet)
myOtherSet.update()
print(myOtherSet)

del myOtherSet
#print(myOtherSet) NameError: name 'myOtherSet' is not defined

mySet = {12, "Azul", "Rojo", 23}
myList = list(mySet)
print(myList)
print(myList[2]) # Es arriesgado porque no se sabe el orden de la lista, ya que cada vez el set dará en orden distinta


myOtherSet = {"Kotlin","Java","Python"}
myNewSet = mySet.union(myOtherSet)
print(myNewSet.union(myNewSet).union(mySet).union({'Javascript', "C#"}))

print(myNewSet.difference(mySet))