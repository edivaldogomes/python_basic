myCondition =  True

if myCondition is True:
    print("Se ejecuta la condición del if")


myCondition = 5 * 2
if myCondition > 10:
    print(("Se ejecuta la condición del segundo if"))
elif(myCondition == 10):
    print("Es igual que 10")
else:
    print("Es menor que 10")

print("La ejecución continua")


myString = ""
if not myString:
    print("Mi cadena está vacía")