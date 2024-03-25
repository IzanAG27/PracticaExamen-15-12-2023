"""
Este programa toma dos números como entrada y
comprueba si el primer número es múltiplo del segundo.
Imprime True si el primer número es múltiplo del segundo,
y False en caso contrario.
"""

def pedir_numeros():
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    return num1, num2


def comprobar_multiplo(num1, num2):
    if num1 % num2 == 0:
        resultado = True

    else:
        resultado = False
    return print(resultado)
