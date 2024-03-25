"""
Este programa toma una frase y la anchura de la pantalla
del usuario como entrada. Luego, centra la frase en la pantalla,
utilizando espacios para llenar el espacio extra.
"""


text = input("Introduce la frase a centrar: ")
ampladaPantalla = int(input("Introduce la mida de la amplada de la pantalla: "))


def escriureCentrat(text, ampladaPantalla):
    num_spaces = int(ampladaPantalla / 2 - len(text) / 2)
    print(' ' * num_spaces + text)
    print(' ' * num_spaces + '=' * len(text))
