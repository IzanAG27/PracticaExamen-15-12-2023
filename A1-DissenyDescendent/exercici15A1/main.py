import kernel

def main():
    cua = []
    while True:
        print("1. Añadir elemento a la cua")
        print("2. Sacar elemento de la cua")
        print("3. Longitud de la cua")
        print("4. Mostrar cua")
        print("5. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            cadena = input("Introduce la cadena a añadir: ")
            kernel.afegeixACua(cadena, cua)
        elif opcion == 2:
            elemento = kernel.treureDeLaCua(cua)
            if elemento is not None:
                print("Elemento sacado:", elemento)
        elif opcion == 3:
            print("Longitud de la cua:", kernel.llargadaCua(cua))
        elif opcion == 4:
            kernel.mostrarCua(cua)
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()