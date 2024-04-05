import time

import SigPunQua
import SigPunPos
import cifCes
import colVocCon
from time import sleep

def main():
    comprobar = True
    while comprobar:
        print("\n1 - Signes puntuació - Quantitat")
        print("2 - Signes puntuació - Posició")
        print("3 - Text - Codificar")
        print("4 - Text - Descodificar")
        print("5 - Executar totes les utilitats")
        print("6 - Sortir de l'aplicacio")

        option = input("Escoge una opción: ")
        if option == '1':
            SigPunPos.calcularLetras()
        elif option == '2':
            SigPunQua.calcular_letras()
        elif option == '3':
            cifCes.cifrarConCesar()
        elif option == '4':
            colVocCon.mostrarTextoPintado()
        elif option == '5':
            SigPunPos.calcular_letras()
            SigPunQua.calcular_letras()
            cifCes.cifrarConCesar()
            colVocCon.mostrar_TextoPintado()
        elif option == '6':
            print("Finalizando programa...")
            time.sleep(2)
            comprobar = False
        else:
            print("\nError: Opción no reconocida.")


if __name__ == "__main__":
    main()
