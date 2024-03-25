import kernel


def main():
    global diccionario
    num_dias = kernel.pedir_dias()
    for i in range(num_dias):
        temp_minima, temp_maxima = kernel.pedir_temperaturas()
        mitjana, diccionario = kernel.calcularTemperaturaMitjana(i+1, temp_minima, temp_maxima)
    print(diccionario)

