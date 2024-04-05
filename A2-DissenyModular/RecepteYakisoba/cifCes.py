"""
   Izan Arnáiz Gallego
   ITB Institut Tecnològic de Barcelona
   ASIXc M03 UF2 A2 Mòduls i Fitxers
   04/04/2024
"""


def obtenerEntrada():
    entrada = input("")
    partes = entrada.split(maxsplit=1)
    return partes


def validarEntrada(partes):
    if len(partes) != 2:
        print("Error: Solo debes proporcionar una clave de desplazamiento y una frase, separados por un espacio.")
        return False
    desplazamiento = partes[0]
    texto = partes[1]
    if not desplazamiento.isdigit():
        print("Error: La clave de desplazamiento debe ser un número entero.")
        return False
    if texto.replace(' ', '').isdigit():
        print("Error: No puedes usar números como palabra.")
        return False
    return True


def cifradoCesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter:
            if caracter.islower():
                desplazamiento_ascii = ord('a')
            else:
                desplazamiento_ascii = ord('A')
            codigo_ascii = ord(caracter)
            nuevo_codigo_ascii = (codigo_ascii - desplazamiento_ascii + desplazamiento) % 26 + desplazamiento_ascii
            caracter_cifrado = chr(nuevo_codigo_ascii)
            resultado += caracter_cifrado
        else:
            resultado += caracter
    return resultado


def cifrarConCesar():
    partes = obtenerEntrada()
    if validarEntrada(partes):
        desplazamiento, texto = partes
        desplazamiento = int(desplazamiento)
        texto_cifrado = cifradoCesar(texto, desplazamiento)
        print(texto_cifrado, "\n")
