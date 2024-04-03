def calcular_media():
    # Implementar la funcionalidad aquí
    pass

def calcular_mediana():
    # Implementar la funcionalidad aquí
    pass

def calcular_desviacion_estandar():
    # Implementar la funcionalidad aquí
    pass

def menu_estadisticas():
    while True:
        print("1 - Calcular mitjana")
        print("2 - Calcular mediana")
        print("3 - Calcular desviació estàndard")
        print("4 - Tornar al menú anterior")
        opcion = float(input("Selecciona una opción: "))
        if opcion == 1.0:
            calcular_media()
        elif opcion == 2.0:
            calcular_mediana()
        elif opcion == 3.0:
            calcular_desviacion_estandar()
        elif opcion == 4.0:
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")