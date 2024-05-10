"""
    Noms: Daniel Arco, Izan Arnaiz.
    Data: 20/03/2024
    Grup: ASIXc1A
    Descripció:
    Módul per a emmagatzemar les funcions per el tractament de paraules boges.
"""

import random
import re
import time
from data_source import *
from colorama import *

init(autoreset=True)


def menu():
    comprobar = True
    print(Fore.CYAN + Style.BRIGHT + "\nMenú:")
    print(Fore.GREEN + "   1. Texto por pantalla")
    print(Fore.GREEN + "   2. Petición a servidor")
    print(Fore.GREEN + "   3. Pregunta a ChatGPT")
    print(Fore.RED + "   4. Salir\n")
    while comprobar:
        opcion = input("")
        if opcion == "1":
            while True:  # Bucle infinito hasta que se introduzca una frase válida
                print("Introduce tu frase:")
                frase = get_data__from_keyboard()
                if len(frase) > 3:
                    print("Aleatorizando...")
                    time.sleep(2)
                    frase = desordenar_frase(frase)
                    return frase
                else:
                    print(Style.BRIGHT + Fore.RED + "La frase no se aleatorizará o tiene que ser de mas de 3 caracteres.")
        elif opcion == "2":
            print("Generando...")
            time.sleep(2)
            frase = get_data_from_server()
            return frase
        elif opcion == "3":
            comprobar = True
            while comprobar:
                questio = input("Introduce tu pregunta: ")
                while not questio.strip():  # Mientras que la pregunta esté vacía
                    print(Style.BRIGHT + Fore.RED + "La pregunta no puede estar vacía. Inténtalo de nuevo.")
                    questio = input("Introduce tu pregunta: ")  # Pide una nueva pregunta
                frase = get_data_from_chatGPT(questio)
                return frase
        elif opcion == "4":
            print("Saliendo...")
            time.sleep(2)
            comprobar = False
            return ""
        else:
            print(Style.BRIGHT + Fore.RED + "Error, introduce un número del 1 al 4.")
            time.sleep(1)
            print("Vuelve a introducir una opción: ")


def ignorar_urls(frase):
    if not isinstance(frase, str):
        frase = str(frase)
    urls = re.findall(r'(http://|https://|ssh@)[^\s]+', frase)
    for i, url in enumerate(urls):
        frase = frase.replace(url, f'URLPLACEHOLDER{i}')
    return frase, urls


def dividir_Palabras(frase, urls):
    return re.split('([^a-zA-Z0-9áéíóúÁÉÍÓÚ])', frase)


def desordenar_palabras(palabra):
    if 'URLPLACEHOLDER' in palabra or (palabra.isdigit() and len(palabra) == 9):
        return palabra
    elif len(palabra) > 3 and (palabra[0].isalnum() and palabra[-1].isalnum()):
        first_char = palabra[0]
        last_char = palabra[-1]
        centro = list(palabra[1:-1])
        random.shuffle(centro)
        return first_char + ''.join(centro) + last_char
    else:
        return palabra


def reconstruir_sentencia(resultado, urls):
    frase_randomizada = ''.join(resultado)
    for i, url in enumerate(urls):
        frase_randomizada = frase_randomizada.replace(f'URLPLACEHOLDER{i}', url)
    return frase_randomizada


def desordenar_frase(frase):
    frase, urls = ignorar_urls(frase)
    palabras = dividir_Palabras(frase, urls)  # Pass urls to the function
    resultado = [desordenar_palabras(palabra) for palabra in palabras]
    return reconstruir_sentencia(resultado, urls)
