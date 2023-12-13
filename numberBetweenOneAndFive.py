"""
Demanar a l'usuari un enter entre 1 i 5.
Si introdueix un número més gran o més petit,
torna-li a demanar l'enter.
Imprimeix per pantalla: El número introduït: 3
substituint el 3 pel número.
input
10
 7
 3
output
El número introduït: 3
"""

comprobar = True

while comprobar:
    num = int(input(""))
    if num > 0 and num < 6:
        comprobar = False
        print("El número introduït es: ", num)
    else:
        print("Introduce un valor entero positivo entre 1 y 5")