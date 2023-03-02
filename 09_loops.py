
# While (condicion)
myCondition = 0
while myCondition < 10:
    print(myCondition)
    #myCondition = myCondition + 1
    myCondition += 2
else:# Es opcional
    print("Mi condición es mayor que 10")


print("La ejecucion continua")

while myCondition < 20:
    myCondition+=2
    if myCondition == 15:
        print("Mi condición es 15")
        break

    print(myCondition)
else:
    print("Mi condición es menor que 20")


## For ##
myList = [35, 24, 62, 52, 30, 30, 17]
print()
print("Aqui empieza el loop for")
for element in myList:
    print(element)



myTuple = (28, 1.80, "Edivaldo", "Gomes")
mySet = {"Armindo", "Machado", 28}
myDict = {"Name": "Mariano", "Surname":"Joaquin", "Edad":28}

print("######################### Tupla #########################")
for i in myTuple:
    print(i)

print("######################### Set #########################")
for j in mySet:
    print(j)

print("######################### Diccionario #########################")
for k in myDict:
    print(k)


print("######################### #########################")
for m in list(myDict.values()):
    print(m)
else:
    print("El bucle for para diccionario ha finalizado")



print()
print("El último bucle comienza aqui")
for element in myDict:
    print(element)
    if element=="Edad":
        continue
        #break
    print("Se ejecuta")
else:
    print("El bucle")