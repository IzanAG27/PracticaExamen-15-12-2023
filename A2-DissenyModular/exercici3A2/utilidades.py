import string
import random
import numpy as np

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros.sort()
    if len(numeros) % 2 == 0:
        mediana = (numeros[len(numeros) // 2 - 1] + numeros[len(numeros) // 2]) / 2
    else:
        mediana = numeros[len(numeros) // 2]
    return mediana

def calcular_desviacion_estandar(numeros):
    media = calcular_media(numeros)
    varianza = sum((numero - media) ** 2 for numero in numeros) / len(numeros)
    return np.sqrt(varianza)

def crazy_words(frase):
    palabras = frase.split()
    resultado = []
    for palabra in palabras:
        if len(palabra) > 3:
            medio = list(palabra[1:-1])
            random.shuffle(medio)
            palabra = palabra[0] + ''.join(medio) + palabra[-1]
        resultado.append(palabra)
    return ' '.join(resultado)

def es_palindromo(frase):
    frase = ''.join(c for c in frase if c not in string.punctuation).replace(' ', '').lower()
    return frase == frase[::-1]

def cifrado_cesar(frase, desplazamiento=3):
    alfabeto = string.ascii_lowercase
    cifrado = ''
    for char in frase:
        if char in alfabeto:
            pos = (alfabeto.find(char) + desplazamiento) % len(alfabeto)
            cifrado += alfabeto[pos]
        else:
            cifrado += char
    return cifrado