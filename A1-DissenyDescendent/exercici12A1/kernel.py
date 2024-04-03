def validarData(dia, mes, any):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > diesDelMes(mes, any):
        return False
    return True

def llegirData():
    while True:
        dia = int(input("Introduce el día: "))
        mes = int(input("Introduce el mes: "))
        any = int(input("Introduce el año: "))
        if validarData(dia, mes, any):
            return dia, mes, any
        else:
            print("Fecha no válida. Inténtalo de nuevo.")

def diesDelMes(mes, any):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes == 2:
        if esAnyDeTraspas(any):
            return 29
        else:
            return 28
    else:
        return 30

def esAnyDeTraspas(any):
    if any % 4 == 0:
        if any % 100 == 0:
            if any % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def calcularDiaJulia(dia, mes, any):
    dia_julia = dia
    for m in range(1, mes):
        dia_julia += diesDelMes(m, any)
    return dia_julia