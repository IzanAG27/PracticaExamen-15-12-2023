import kernel


def main():
    while True:
        print("1. Convertir segons a hores, minuts i segons")
        print("2. Convertir hores, minuts i segons a segons")
        print("3. Sortir")
        opcio = int(input("Tria una opció: "))
        if opcio == 1:
            segons = int(input("Introdueix segons: "))
            hores, minuts, segons = kernel.segons_a_hms(segons)
            print(f"{hores} hores, {minuts} minuts, {segons} segons")
        elif opcio == 2:
            hores = int(input("Introdueix hores: "))
            minuts = int(input("Introdueix minuts: "))
            segons = int(input("Introdueix segons: "))
            segons = kernel.hms_a_segons(hores, minuts, segons)
            print(f"{segons} segons")
        elif opcio == 3:
            break
        else:
            print("Opció no vàlida. Torna a intentar-ho.")


if __name__ == "__main__":
    main()
