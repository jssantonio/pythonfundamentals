cadena = "Diferentes Metodos para las Cadenas"

print (cadena.lower()) #lower pone todo en minusculas 
print (cadena.upper()) #upper pone todo en mayusculas
print (cadena.capitalize()) #solo la primer letra del texto en mayuscula
print (cadena.title()) #cada inicio de palabra las pone en mayusculas 
print (cadena.swapcase()) #intercala mayusculas por minusculas y viceversa

#Ejercicio
ejercicio = "Te quiero solo como amigo"
print (ejercicio [0 : 2]) #Imprima los dos primeros caracteres.
print (ejercicio [-2 : ]) #Imprima los dos ultimos caracteres.
print (ejercicio [: : 2]) #Imprima cada dos caracteres
print (ejercicio [: : -1]) #Imprime el texto a la inversa 
print (ejercicio + ejercicio [: : -1]) #Imprime el texto normal y despues a la inversa