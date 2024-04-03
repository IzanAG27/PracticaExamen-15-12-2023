import estadisticas
import cadenas


def main():
    while True:
        print("1 - Utilitats Estadístiques")
        print("2 - Utilitats de Cadenes")
        print("3 - Sortir de l’aplicació")
        opcion = float(input("Selecciona una opción: "))
        if opcion == 1.0:
            estadisticas.menu_estadisticas()
        elif opcion == 2.0:
            cadenas.menu_cadenas()
        elif opcion == 3.0:
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
