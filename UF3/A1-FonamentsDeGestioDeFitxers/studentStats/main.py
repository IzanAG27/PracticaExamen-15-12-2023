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
        numbers = list(map(int, lineas[i].split()))
        numbers.sort()
        lineas[i] = ' '.join(map(str, numbers))
    return '\n'.join(lineas)


def calcular_notas(resultado):
    lineas = resultado.split('\n')
    for i in range(len(lineas)):
        numbers = list(map(int, lineas[i].split()))
        nota_minima = min(numbers)
        nota_maxima = max(numbers)
        nota_media = sum(numbers) / len(numbers)
        print(f'Nota mínima: {nota_minima}\nNota máxima: {nota_maxima}\nNota mitjana: {nota_media}')

directorio = pedir_directorio()
if directorio is not None:
    lineas = recorrer_archivo(directorio)
    resultado = ordenar_nums(lineas)
    calcular_notas(resultado)

contenido = pedir_directorio()
resultado = ordenar_nums(contenido)
print(resultado)

