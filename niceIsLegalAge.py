


try:
    comprobar = True
    while comprobar == True:
        edad = int(input(""))
        if edad >= 18:
            print("Eres mayor de edad")
            comprobar = False
        elif edad < 18 and edad > 0:
            print("Eres menor de edad")
            comprobar = False
        else:
            print("Introduce bien los datos")
except ValueError:
    print("Introduce bien los datos")
finally:
    print("Programa terminado")
