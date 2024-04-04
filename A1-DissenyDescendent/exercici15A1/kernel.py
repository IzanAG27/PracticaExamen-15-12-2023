def llargadaCua(cua):
    return len(cua)

def estaBuidaCua(cua):
    return len(cua) == 0

def afegeixACua(cadena, cua):
    cua.append(cadena)

def treureDeLaCua(cua):
    if estaBuidaCua(cua):
        print("Error: la cua está vacía.")
        return None
    else:
        return cua.pop(0)

def mostrarCua(cua):
    if estaBuidaCua(cua):
        print("La cua está vacía.")
    else:
        print("Primer elemento:", cua[0])
        print("Último elemento:", cua[-1])
        print("Cua completa:", ' '.join(cua))