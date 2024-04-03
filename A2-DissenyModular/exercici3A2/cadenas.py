def crazy_words():
    # Implementar la funcionalidad aquí
    pass

def es_palindromo():
    # Implementar la funcionalidad aquí
    pass

def cifrado_cesar():
    # Implementar la funcionalidad aquí
    pass

def menu_cadenas():
    while True:
        print("1 - Crazy Words")
        print("2 - És una frase palindroma?")
        print("3 - Xifratge de Cèsar")
        print("4 - Tornar al menú anterior")
        opcion = float(input("Selecciona una opción: "))
        if opcion == 1.0:
            crazy_words()
        elif opcion == 2.0:
            es_palindromo()
        elif opcion == 3.0:
            cifrado_cesar()
        elif opcion == 4.0:
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")