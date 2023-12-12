
"""
Escriu un programa que llegeixi un nombre natural
més petit que 256 i escrigui la seva representació en binari.
"""
try:
    comprobar = True
    while comprobar == True:
        num = int(input(""))
        if num < 256:
            print(bin(num))
            comprobar = False
        else:
            print("Escribe un número entero positivo menor o igual que 256")
except ValueError:
    print("Introduce correctamente los valores")
finally:
    print("Programa terminado ^-^")