myDict = dict()
myOtherDict = {}

print(type(myDict))
print(type(myOtherDict))

myOtherDict = {"id":1, "name": "Edivaldo", "age":28, "surname":"Gomes"}
print(myOtherDict)


myDict = {
    "id":1,
    "name": "Edivaldo",
    "age":28,
    "surname":"Gomes",
    "lenguages": {'Python', 'Swift', 'Kotlin'}
}

print(myDict)
print(len(myDict))
print(len(myDict))

print(myDict["name"])
myDict["name"] = "Mariano"
myDict["calle"]="Doctor Alvaro"
print(myDict)

del myDict["calle"]
print(myDict)

print("name" in myOtherDict) 

print(myDict.keys())
print(myDict.items())
print(myDict.values())

print()
myList = ["name", 1, "Piso"]
myNewDict = dict.fromkeys((myList))
print(myNewDict)

myNewDict = dict.fromkeys(("Name", 1, "Piso"))
print(myNewDict)

myNewDict = dict.fromkeys(myDict)
print(myNewDict)

myNewDict = dict.fromkeys(myDict, "Edivaldo")
print(myNewDict)


print(myNewDict.values())
print("Lista: ", list(myNewDict.values()))
print("Tupla: ", tuple(myNewDict))
print("SET: ",set(myNewDict))