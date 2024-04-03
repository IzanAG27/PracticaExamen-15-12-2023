import kernel

def main():
    while True:
        print("1. Sumar dos fracciones")
        print("2. Restar dos fracciones")
        print("3. Multiplicar dos fracciones")
        print("4. Dividir dos fracciones")
        print("5. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion in [1, 2, 3, 4]:
            print("Introduce la primera fracción:")
            n1, d1 = kernel.llegirFraccio()
            print("Introduce la segunda fracción:")
            n2, d2 = kernel.llegirFraccio()
            if opcion == 1:
                n, d = kernel.sumarFraccions(n1, d1, n2, d2)
            elif opcion == 2:
                n, d = kernel.restarFraccions(n1, d1, n2, d2)
            elif opcion == 3:
                n, d = kernel.multiplicarFraccions(n1, d1, n2, d2)
            else:
                n, d = kernel.dividirFraccions(n1, d1, n2, d2)
            print("El resultado es:")
            kernel.escriureFraccio(n, d)
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()