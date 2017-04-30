def numerocien():
    numero = int(input("Ingresa un número: "))
    intentos = 1
    while intentos <= 10000:
        if numero == 100:
            print("El número es 100")
            intentos = 10000
        else:
            if numero > 100:
                print("El número es menor que", numero)
                numero = int(input("Intenta de nuevo: "))
            elif type(numero) == str:
                print("Debe ser un número")
                numero = int(input("Otro intento: "))
            else:
                print("El número es mayor que", numero)
                numero = int(input("Sigue intentando: "))
        intentos = intentos + 1


numerocien()
print("¡VUELVE PRONTO!")