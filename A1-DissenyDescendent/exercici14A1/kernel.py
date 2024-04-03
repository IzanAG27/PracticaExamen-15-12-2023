"""
Funcions
"""
def llargadaPila(pila):
    return len(pila)

def estaBuidaPila(pila):
    return len(pila) == 0

def afegeixAPila(cadena, pila):
    pila.append(cadena)

def treureDeLaPila(pila):
    if estaBuidaPila(pila):
        print("Error: la pila está vacía.")
        return None
    else:
        return pila.pop()

def mostrarPila(pila):
    if estaBuidaPila(pila):
        print("La pila está vacía.")
    else:
        print("Primer elemento:", pila[0])
        print("Último elemento:", pila[-1])
        print("Pila completa:", pila)