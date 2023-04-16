nombre = input ('Ingresa tu nombre: ')
edad = int (input('Ingresa tu edad: '))
print (nombre)
print (edad)

#Otra manera de imprimir con {} y .format
name = input ("Escribe tu nombre: ")
age = int (input ("Escribe tu edad: "))
print ("Hola {} tienes {}".format(name,age))


#Ejercicio de formula general x= -b +- sqrt b ** 2 - 4ac / 2a
from math import sqrt #Estamos importanto la libreria matematica math para hacer uso de la reiaz cuadrada que es sqrt 

a = int (input('Ingresa el valor de a: '))
b = int (input ('Ingresa el valor de b: '))
c = int (input ('Ingresa el valor de c: '))
x1 = 0
x2 = 0

if ((b**2) - (4*a*c)) < 0:
    print ("'Error' ya que no se puede sacar raiz a un numero negativo")
else:
    x1 = (-b + sqrt ((b**2) - (4*a*c))) / (2*a)
    x2 = (-b - sqrt ((b**2) - (4*a*c))) / (2*a)
    print ("El resultado es: \nx1=", x1, "\nx2=", x2)

#Ejercicio
nombre = input ("Ingresa tu nombre: ")
edad = int (input("Ingresa tu edad: "))
sexo = input ("Ingresa tu sexo: ")
print ("Te llamas: ", nombre, "\nTu edad es: ", edad, "\nTu sexo es: ", sexo)

#Ejercicio
vocal = input ("Ingresa una vocal en minuscula: ")
consonante = input ("Ingresa una consonante en mayuscula: ")
print (vocal.upper(), consonante.lower())