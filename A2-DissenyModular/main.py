import caLL
import VyC
import cifCes
import colVocCon
import SystemColors


def main():
    exit_app = False
    while not exit_app:
        print("1 - Signes puntuació - Quantitat")
        print("2 - Signes puntuació - Posició")
        print("3 - Text - Codificar")
        print("4 - Text - Descodificar")
        print("5 - Executar totes les utilitats")
        print("6 - Sortir de l'aplicacio")

        option = input("Escoge una opción: ")
        if option == '1':
            print("Ejecutando 'Signes puntuació - Quantitat'...")
            caLL.calcular_letras()
        elif option == '2':
            print("Ejecutando 'Signes puntuació - Posició'...")
            VyC.calcular_letras()  # Llama a la función sin verificar ningún valor retornado
        elif option == '3':
            print("Ejecutando 'Text - Codificar'...")
            cifCes.cifrar_texto_con_cesar()
        elif option == '4':
            print("Ejecutando 'Text - Descodificar'...")
            colVocCon.mostrar_texto_pintado()
        elif option == '5':
            print("Ejecutando 'Executar totes les utilitats'...")
            caLL.calcular_letras()
            VyC.calcular_letras()
            cifCes.cifrar_texto_con_cesar()
            colVocCon.mostrar_texto_pintado()
        elif option == '6':
            print("Finalizando aplicación...")
            exit_app = True
        else:
            print("Opción no reconocida. Porfavor, inténtalo de nuevo.")


if __name__ == "__main__":
    main()
