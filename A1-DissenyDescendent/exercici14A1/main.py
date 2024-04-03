"""
Execució programa principal
"""
import kernel

comprobar = True
while comprobar:
    opcion = kernel.menu()
    if opcion == 1:
        cadena = input("Introduce la cadena a añadir a la pila: ")
        kernel.afegeixAPila(cadena, kernel.pila, 10)
    elif opcion == 2:
        elemento = kernel.treureDeLaPila(kernel.pila)
        if elemento is not None:
            print("Elemento retirado de la pila: ", elemento)
    elif opcion == 3:
        print("Longitud de la pila: ", kernel.llargadaPila(kernel.pila))
    elif opcion == 4:
        kernel.mostrarPila(kernel.pila)
    elif opcion == 5:
        comprobar = False
    else:
        print("Número inválido!")
        comprobar = False