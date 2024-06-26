"""
Execució programa principal
"""
import kernel

def main():
    pila = []
    while True:
        print("1. Añadir elemento a la pila")
        print("2. Sacar elemento de la pila")
        print("3. Longitud de la pila")
        print("4. Mostrar pila")
        print("5. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            cadena = input("Introduce la cadena a añadir: ")
            kernel.afegeixAPila(cadena, pila)
        elif opcion == 2:
            elemento = kernel.treureDeLaPila(pila)
            if elemento is not None:
                print("Elemento sacado:", elemento)
        elif opcion == 3:
            print("Longitud de la pila:", kernel.llargadaPila(pila))
        elif opcion == 4:
            kernel.mostrarPila(pila)
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()