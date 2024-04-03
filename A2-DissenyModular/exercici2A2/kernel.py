from penjat import penjat
from enfonsarLaFlota import enfonsarLaFlota
from buscamines import buscamines
from tresEnRatlla import tresEnRatlla


def escoger_opcion():
    print("1 - El penjat")
    print("2 - El 3 en ratlla")
    print("3 - Buscamines")
    print("4 - Enfonsar la flota")
    print("5 - Sortir de l'aplicacio")

    opcion = int(input("Selecciona una opción: "))
    return opcion


def ejecutar_opcion(opcion):
    comprobar = True
    while comprobar:
        if opcion == 1:
            penjat.play_game()
        elif opcion == 2:
            tresEnRatlla.play_game()
        elif opcion == 3:
            buscamines.play_game()
        elif opcion == 4:
            enfonsarLaFlota.play_game()
        elif opcion == 5:
            print("Saliendo de la aplicación...")
            comprobar = False
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")


