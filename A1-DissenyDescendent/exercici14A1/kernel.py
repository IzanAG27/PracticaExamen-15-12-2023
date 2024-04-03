"""
Funcions
"""
pila = []


from colorama import Fore, Style

def menu():
    print(Fore.GREEN + "Menu:")
    print(Fore.YELLOW + "  1. Afegir element a la pila")
    print(Fore.YELLOW + "  2. Treure element de la pila")
    print(Fore.YELLOW + "  3. Longuitud de la pila")
    print(Fore.YELLOW + "  4. Mostrar pila")
    print(Fore.YELLOW + "  5. Sortir" + Style.RESET_ALL)
    opcion = int(input("Elige una opción: "))
    return opcion

def afegeixAPila(cadena, pila, max_size):
    if len(pila) < max_size:
        pila.append(cadena)
        print(Fore.GREEN + "Elemento añadido a la pila." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Error: La pila está llena." + Style.RESET_ALL)
    return pila

def treureDeLaPila(pila):
    if len(pila) == 0:
        print(Fore.RED + "Error: La pila está vacía." + Style.RESET_ALL)
        return None
    else:
        elemento = pila.pop()
        print(Fore.GREEN + "Elemento retirado de la pila: " + elemento + Style.RESET_ALL)
        return elemento

def mostrarPila(pila):
    if len(pila) == 0:
        print(Fore.RED + "La pila está vacía." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Primer elemento: " + pila[0])
        print("Último elemento: " + pila[-1])
        print("Pila completa: " + str(pila) + Style.RESET_ALL)