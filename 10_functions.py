
def myFunction ():
    print("Hola nueva funcion")

def suma (a, b):
    return a + b

def suma2 (firstValue, secondValue):
    print("La suma de dos valores es: ", firstValue+secondValue)

def print_name(name, surname):
    print(f"{name} {surname}")

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name("Gomes","Edivaldo")
print_name(surname="Gomes", name="Edivaldo")
print_name_with_default(surname="Gomes", name="Edivaldo")


myFunction()
suma2(85, 12)
print(suma(12, 55))

# Paratros dinamicos
def print_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_texts("Hola", "python", "Java")


