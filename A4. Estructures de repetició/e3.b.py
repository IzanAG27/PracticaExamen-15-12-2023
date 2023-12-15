"""
Escriu un programa que demani números per teclat fins que s'introdueix un zero.
El programa haurà d'imprimir la suma i la mitjana de tots els números introduïts.
"""

suma = 0
contador = 0
numero = float(input("Introduce un número (introduce 0 para terminar): "))

while numero != 0:
    suma += numero
    contador += 1
    numero = float(input("Introduce un número (introduce 0 para terminar): "))

if contador > 0:
    media = suma / contador
    print(f"La suma de los números introducidos es: {suma}")
    print(f"La media de los números introducidos es: {media}")
else:
    print("No se introdujeron números.")
