myStringVariable = "Hello"
mySecondVariable = True

print(myStringVariable, str(mySecondVariable))
print(type(myStringVariable))
print(type(str(mySecondVariable)))
print(type(mySecondVariable))


name, surname, alias, age = "Edivaldo", "Gomes", "Edni", 28
print("Me llamo: ", name, surname,". Mi edad es: ", age,". Y mi alias es: ", alias)


def Person(name, age):
    return f"{name} tiene {age} años de edad"


name = "Edivaldo"
age = 28
print(Person(name, age))

address : str = "Doctor Maranez"# Tipado debil
print(address)
print(type(address))


