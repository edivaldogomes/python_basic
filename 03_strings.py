myString = "Mi String"
myOtherString = "Mi otro String"

print(len(myString))
print(len(myOtherString))
print(myString+ " " + myOtherString)
myStringOtherLine = "Este String se pondrá \n en otra linnea"
print(myStringOtherLine)
myStringtabLine = "\tEste String tiene tabulación"
print(myStringtabLine)

name,surname, age = "Edivaldo", "Gomes", 28
print(f"Mi nombre es {name} {surname} y tengo {age} anos")
print("Mi nombre es " + name + " " + surname + "y tengo " + str(age) + " "+ "anos")
print("Mi nombre es {} {} y tengo {} anos".format(name, surname, age))
print("Mi nombre es %s %s y tengo %d anos" %(name, surname, age ))

# Desempaquetado de caracter
language = "Python"
a, b, c, d, e,f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division
languageSlice = language[1:3]
print(languageSlice)
languageSlice = language[1:]
print(languageSlice)
languageSlice = language[0:6:2]
print(languageSlice)




# Reverse
reversedLanguaje = language[::-1]
print(reversedLanguaje)

#Funciones

print(language.upper())
print(language.lower())
print(language.find("o"))
print(language.capitalize())
print(language.count("o"))
print(language.isnumeric())
print(language.upper().isupper())
print(language.startswith("Py"))