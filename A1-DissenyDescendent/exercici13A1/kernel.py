def calcularMCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def simplificarFraccio(numerador, denominador):
    mcd = calcularMCD(numerador, denominador)
    return numerador // mcd, denominador // mcd


def llegirFraccio():
    numerador = int(input("Introduce el numerador: "))
    denominador = int(input("Introduce el denominador: "))
    return simplificarFraccio(numerador, denominador)


def escriureFraccio(numerador, denominador):
    if denominador == 1:
        print(numerador)
    else:
        print(f"{numerador}/{denominador}")


def sumarFraccions(n1, d1, n2, d2):
    return simplificarFraccio(n1 * d2 + d1 * n2, d1 * d2)


def restarFraccions(n1, d1, n2, d2):
    return simplificarFraccio(n1 * d2 - d1 * n2, d1 * d2)


def multiplicarFraccions(n1, d1, n2, d2):
    return simplificarFraccio(n1 * n2, d1 * d2)


def dividirFraccions(n1, d1, n2, d2):
    return simplificarFraccio(n1 * d2, d1 * n2)
