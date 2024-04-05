def obtenerCodigo():
    return input("Por favor, ingresa el código separado por puntos: ")


def convertirAscii(codigo):
    partes = codigo.split(".")
    mensaje = ""
    for parte in partes:
        if parte.isdigit():
            numero = int(parte)
            if 0 <= numero <= 0x10FFFF:
                mensaje += chr(numero)
            else:
                print(f"El código {numero} está fuera del rango válido para la conversión a ASCII.")
                return
        else:
            print("El código debe ser una secuencia de números separados por puntos.")
            return
    print("El mensaje ASCII es:", mensaje)


codigo = obtenerCodigo()
convertirAscii(codigo)
