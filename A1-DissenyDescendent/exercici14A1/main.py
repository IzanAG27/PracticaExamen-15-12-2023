"""
Execució programa principal
"""
import kernel

comprobar = True
while comprobar:
    if kernel.menu() == 1:
        kernel.afegeixAPila()
    elif kernel.menu() == 2:
        kernel.treureDeLaPila()
    elif kernel.menu() == 3:
        kernel.llargadaPila()
    elif kernel.menu() == 4:
        kernel.mostrarPila()
    elif kernel.menu() == 5:
        comprobar = False
    else:
        print("Número inválido!")
        comprobar = False
