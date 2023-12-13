import random
comprobar = True
cont = 0
while comprobar:
    aleatori = random.randint(1,100)
    num = int(input(""))
    if num > 0 and num < 100:
        if num == aleatori:
            comprobar = False
            print("Has acertado")
        elif num < aleatori:
            cont += 1
            print("El número aleatorio es mas grande")
        elif num > aleatori:
            cont += 1
            print("El numero aleatorio es mas pequeño")
        print("El numero aleatorio es: ", aleatori)
        print("Te quedan ", 10 - cont," intentos.")
    else:
        print("El numero es inválido")
