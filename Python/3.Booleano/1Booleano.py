verdadero = True
falso = False

print (type (verdadero))
print (type (falso))

#Booleanos en strings 

cadena = ("Este es un ejemplo de booleanos en strings")
print (cadena.startswith("E")) #startswith significa que la cadena empieza con E por eso da True
print (cadena.endswith("s")) #endswith significa que la cadena termina con s por eso da True
print (cadena.isupper()) #False porque no está todo en mayusculas
print (cadena.islower()) #False porque no todo está enminusculas 