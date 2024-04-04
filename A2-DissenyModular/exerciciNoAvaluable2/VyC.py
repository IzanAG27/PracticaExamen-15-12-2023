def contar_vocales_y_consonantes(frase):
    vocales = 'aeiou'
    letras = {}
    for i, letra in enumerate(frase.lower(), start=1):
        if letra.isalpha():
            if letra in vocales:
                tipo = 'vocal'
            else:
                tipo = 'consonante'
            if letra not in letras:
                letras[letra] = {'tipo': tipo, 'cantidad': 1, 'posiciones': [i]}
            else:
                letras[letra]['cantidad'] += 1
                letras[letra]['posiciones'].append(i)
    return letras


def validar_frase(frase):
    palabras = frase.split()
    return len(palabras)


def calcular_letras():
    seguir = True
    while seguir:
        frase = input("")
        if frase == "\\q":
            seguir = False
        elif not validar_frase(frase):
            print("La frase debe contener más de dos palabras.")
        else:
            letras = contar_vocales_y_consonantes(frase)
            print("Lletra    Quantitat    Posició")
            for letra, datos in letras.items():
                print(
                    f"{letra}         {datos['cantidad']}            {', '.join(map(str, datos['posiciones']))}")


calcular_letras()
