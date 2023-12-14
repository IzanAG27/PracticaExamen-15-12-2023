
cadena = input("Cadena: ")
caracter_original = input("Caracter que quieres cambiar: ")
caracter_nuevo = input("Que caracter quieres poner: ")
for char in str(cadena):
    if caracter_original == char:
        char = caracter_nuevo
    print(char, end="")
