# Crear una lista de cadenas de caracteres
lista_cadenas = []

while True:
    # Mostrar el menú de opciones
    print("\nMenú de opciones:")
    print("1. Comptar")
    print("2. Modificar")
    print("3. Suprimir")
    print("4. Mostrar")
    print("5. Sortir")

    # Solicitar al usuario que elija una opción
    opcion = input("Selecciona una opció (1-5): ")

    # Verificar la opción seleccionada
    if opcion == "1":
        # Comptar: contar la cantidad de veces que aparece una cadena en la lista
        cadena_buscar = input("Introdueix la cadena a comptar: ")
        contador = lista_cadenas.count(cadena_buscar)
        print(f"{cadena_buscar} apareix {contador} vegades a la llista.")

    elif opcion == "2":
        # Modificar: reemplazar cada aparición de la primera cadena con la segunda
        cadena_original = input("Introdueix la cadena original: ")
        cadena_nueva = input("Introdueix la nova cadena: ")
        lista_cadenas = [cadena_nueva if cadena == cadena_original else cadena for cadena in lista_cadenas]
        print("La llista s'ha modificat.")

    elif opcion == "3":
        # Suprimir: eliminar una cadena de la lista
        cadena_eliminar = input("Introdueix la cadena a suprimir: ")
        if cadena_eliminar in lista_cadenas:
            lista_cadenas.remove(cadena_eliminar)
            print(f"{cadena_eliminar} s'ha eliminat de la llista.")
        else:
            print(f"{cadena_eliminar} no es troba a la llista.")

    elif opcion == "4":
        # Mostrar: mostrar las cadenas en la lista
        print("Llista de cadenes:")
        for cadena in lista_cadenas:
            print(cadena)

    elif opcion == "5":
        # Salir del programa
        print("Adéu!")
        break

    else:
        print("Opció no vàlida. Si us plau, introdueix un nombre entre 1 i 5.")
