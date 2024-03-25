text = input("Introduce la frase a centrar: ")
ampladaPantalla = int(input("Introduce la mida de la amplada de la pantalla: "))


def escriureCentrat(text, ampladaPantalla):
    num_spaces = int(ampladaPantalla / 2 - len(text) / 2)
    print(' ' * num_spaces + text)
    print(' ' * num_spaces + '=' * len(text))
