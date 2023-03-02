class MyEmptyPerson:
    pass

class Person:
    def __init__(self, name, surname, alias="Sin alias") -> None:
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname} {alias}"

    def walk (self):
        print(f"{self.full_name} está caminando")


print(MyEmptyPerson())
print(MyEmptyPerson)

my_person = Person("Edivaldo", "Gomes")

print(f"{my_person.name} {my_person.surname}")
print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)
my_person.walk()

print("################## Second Person ###########################")

my_other_person = Person("Armindo", "Machado", "Ednicolaevicth")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Ahora ya cambio todo"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)



########  Get y Settter #############33

# En constructor

"""
Permite que solo se pueda crear y no modificar

self.__name # Propiedad privada
self.__surname

def get_name (self):
    return self.__name

def get_surname (self):
    return self.__surname



"""


