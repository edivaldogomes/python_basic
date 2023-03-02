numberOne, numberTwo = 2, 1

# Try except
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# Try except else

try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("la ejecuión continua correctamente")


# Try except else finally

try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no produce una excepción
    print("La ejecuión continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecución continua")


# Captura de la información de la excepción
first, second = "Hola", 6
try:
    print(first + second)
except ValueError:
    print("Se ha producido un value error")
except TypeError:
    print("Se ha producido un type error")


first, second = "Hola", 6
try:
    print(first + second)
except TypeError as error:
    print(error)
except Exception as exception:
    print(exception)