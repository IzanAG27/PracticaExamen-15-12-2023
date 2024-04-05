import time
import SigPunQua
import SigPunPos
import cifCes
import colVocCon


def main():
    comprobar = True
    while comprobar:
        print("")
        option = input("Escoge una opción: ")
        if option == '1':
            SigPunQua.calcularLetras()
        elif option == '2':
            SigPunPos.calcularLetras()
        elif option == '3':
            cifCes.cifrarConCesar()
        elif option == '4':
            colVocCon.mostrarTextoPintado()
        elif option == '5':
            SigPunQua.calcularLetras()
            SigPunPos.calcularLetras()
            cifCes.cifrarConCesar()
            colVocCon.mostrarTextoPintado()
        elif option == '6':
            print("Finalizando programa...")
            time.sleep(2)
            comprobar = False
        else:
            print("\nError: Opción no reconocida.")


if __name__ == "__main__":
    main()
