import kernel

try:
    def main():
        radi = float(input("Introdueix el radi de la circumferència: "))
        area = kernel.calcularArea(radi)
        perimetre = kernel.calcularPerimetre(radi)
        print("L'àrea de la circumferència és: ", round(area, 2))
        print("El perímetre de la circumferència és: ", round(perimetre, 2))
except ValueError:
    print("Introduce valores correctos, enteros o flotantes positivos.")

if __name__ == "__main__":
    main()
