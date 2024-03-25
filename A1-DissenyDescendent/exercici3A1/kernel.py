"""
Este programa registra y calcula la temperatura media
a lo largo de varios días. El usuario introduce el número
de días y las temperaturas mínima y máxima para cada día.
Luego, el programa calcula la temperatura media para cada
día y la almacena en un diccionario.
"""

def pedir_dias():
    num_dias = int(input("Introduce el numero de dias: "))
    return num_dias


def pedir_temperaturas():
    temp_minima = float(input("Temperatura minima: "))
    temp_maxima = float(input("Temperatura maxima: "))
    return temp_minima, temp_maxima


def calcularTemperaturaMitjana(num_dias, temp_minima, temp_maxima):
    diccionario = {}
    mitjana = (temp_minima + temp_maxima) / 2
    for x in range(1, num_dias + 1):
        diccionario[x] = mitjana
        print(f"La temperatura media del dia {x} es {mitjana}")
    return mitjana, diccionario