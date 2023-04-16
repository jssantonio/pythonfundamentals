#Ejercicio 1:
'''vocal = input ("Ingrese una vocal: ")

if vocal.lower () == "a":
    print ("Es una vocal")
elif vocal.lower () == "e":
    print ("Es una vocal")
elif vocal.lower () == "i":
    print ("Es una vocal")
elif vocal.lower () == "o":
    print ("Es una vocal")
elif vocal.lower () == "u":
    print ("Es una vocal")
else:
    print ("No es una vocal")

#Otra forma de realizarlo de forma simplificada es:
vocal2 = input ("Escribe una vocal ")

if vocal2.lower() in "aeiou":
    print ("Es una vocaal")
else:
    print ("No es una vocal")

#Ejercicio 2 
numero = int (input ("Escribe un numero ENTERO: "))

if numero >= 0:
    print ("El valor absoluto de :", numero, "es",  numero)
else:
    print ("El valor absoluto de: ", numero, "es", numero * -1)

#Otra forma de realizarlo de forma simplificada es:
print (abs (10)) #abs te arroja el valor absoluto del numero 
print (abs (-189)) #abs te arroja el valor absoluto del numero en positivo, el valor absoluto es siempre positivo

#Ejercicio 3
word1 = (input ("Escribe la palabra: "))
word2 = (input ("Escribe la palabra: "))

if len (word1) < 3 or len (word2) < 3:
    print ("No aplica porque la palabra tiene menos de 3 caracteres")
elif word1 [-3 : ] == word2 [-3 : ]:
    print ("Las palabras riman")
elif word1 [-2 : ] == word2 [-2 : ]:
    print ("Las palabras riman un poco")
else:
    print ("Las palabras no riman")'''
