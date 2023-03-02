# La gran diferencia es que las tupulas son imutables, ya sean no se pueden cambiar los valores.
myTuple = tuple()

myOtherTupla = ()
myOtherTupla = (23,24,54,7)

myTuple = (28, 1.80, "Edivaldo", "Gomes")
print(myTuple)
age, height, name, surname = myTuple
print(age)

for i in myTuple:
    print(i)

print()
print(myTuple.count("Edivaldo"))
print(myTuple.index("Gomes"))
# myTuple[1]= 1.80 'tuple' object does not suppport  item assignment
mySumTuple = myTuple + myOtherTupla
print(mySumTuple[3:6])
myTuple = list(myTuple)
myTuple.insert(1,"Azul")
print("La nueva lista es: ", myTuple)

del myTuple #NameError: name 'myTuple' is not defined
#print(myTuple) #Es un error que no creo que sea correcto porque ya de esta forma estariamos modificando la tupla# 