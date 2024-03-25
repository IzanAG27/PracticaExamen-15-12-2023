def pedir_cadena():
    cadena = input("Texto: ")
    return cadena


def afegirEspaiACadaCaracter(cadena):
    lista = []
    if cadena:  # Comprueba si la cadena no está vacía
        for x in cadena:
            lista.append(x)
        cadena_sin_espacios = ' '.join(lista)
        print(cadena_sin_espacios)
    else:
        print("La cadena está vacía")
    return lista