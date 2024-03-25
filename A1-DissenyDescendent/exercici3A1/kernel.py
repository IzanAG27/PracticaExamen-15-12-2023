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