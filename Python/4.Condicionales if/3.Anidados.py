nombre = input ("Ingresa tu nombre: ")
edad = int (input ("Teclea tu edad: "))

if nombre == "Jesus":
    if edad >= 18:
        print ("Eres Jesús y eres mayor de edad")
    else:
        print ("Eres Jesús pero no eres mayor de edad")
else:
    print ("Tú no eres Jesús")
