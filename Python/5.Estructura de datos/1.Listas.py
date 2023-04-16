#Las listas son modificables 
listas = ["Las listas", 123, "son", 456, "modificables"]
print (listas)
print (listas[3], "\n")

listas [4] = "editables"
print (listas)
print (listas[1], "\n")

#Para agregar valores a las listas
listas2 = [1, 2, 3, 4, 5, 6]

#listas2.append (7) #se agrega el no. 7 al final de la lista 
#print (listas2)

listas2.insert (6, 8)
print (listas2)