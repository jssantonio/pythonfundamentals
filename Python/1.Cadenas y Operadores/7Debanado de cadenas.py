substring = "Este es un ejemplo de SUBSTRING (Debanado de cadenas)"
print (len(substring)) #len devuelve el tamaño de la cadena


substring2 = "Este es un ejemplo de SUBSTRING (Debanado de cadenas)"
print (substring2 [5]) #Muestra el caracter numero 5 
print (substring2 [5 : 10]) #Muestra los caracteres del 5 al 8 
print (substring2 [0 : 32]) #Del cero al 32
print (substring2 [20 : ]) #Del 20 al final
print (substring2 [-10]) #Empieza desde el final

#Ejercicio
ejercicio = "Te quiero solo como amigo"
print (ejercicio [0 : 2]) #Imprima los dos primeros caracteres.
print (ejercicio [-2 : ]) #Imprima los dos ultimos caracteres.
print (ejercicio [: : 2]) #Imprima cada dos caracteres
print (ejercicio [: : -1]) #Imprime el texto a la inversa 
print (ejercicio + ejercicio [: : -1]) #Imprime el texto normal y despues a la inversa

palabra = "\nseparado\n"
print (palabra)

newpalabra = palabra.replace ("a" , "A") #Todas las letras a serán reemplazadas por letras mayusculas A
print (newpalabra)

newpalabra2 = palabra.replace ("" , ",") #Imprilo en los espacios en blaco de cada letra por ","
print (newpalabra2)