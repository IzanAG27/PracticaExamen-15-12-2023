import os


def pedir_directorio():
    fitxer = input("")
    if not os.path.exists(fitxer):
        print("Introduce un archivo válido")
    else:
        return fitxer


def recorrer_archivo(directorio):
    with open(directorio, 'r', encoding='UTF-8') as archivo:
        lineas = archivo.read().splitlines()
    return lineas


def ordenar_nums(lineas):
    for i in range(len(lineas)):
        numeros = list(map(int, lineas[i].split()))
        numeros.sort()
        lineas[i] = ' '.join(map(str, numeros))
    return '\n'.join(lineas)


def calcular_notas(resultado):
    lineas = resultado.split('\n')
    for i in range(len(lineas)):
        numeros = list(map(int, lineas[i].split()))
        nota_minima = numeros[0]
        nota_maxima = numeros[-1]
        nota_media = round(sum(numeros) / len(numeros), 1)
        print(f'Nota mínima: {nota_minima}\nNota màxima: {nota_maxima}\nNota mitjana: {nota_media}')


directorio = pedir_directorio()
if directorio is not None:
    lineas = recorrer_archivo(directorio)
    resultado = ordenar_nums(lineas)
    calcular_notas(resultado)

contenido = pedir_directorio()
resultado = ordenar_nums(contenido)
print(resultado)
