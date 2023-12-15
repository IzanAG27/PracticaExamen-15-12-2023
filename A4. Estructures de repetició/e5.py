numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))

# Asegurándonos de trabajar con valores absolutos
a = abs(numero1)
b = abs(numero2)

# Inicializando el resultado en cero
resultado = 0

# Realizando la multiplicación mediante sumas
for n in range(b):
    resultado += a

# Ajustando el signo del resultado según los números ingresados
if (numero1 < 0 and numero2 > 0) or (numero1 > 0 and numero2 < 0):
    resultado = -resultado

print(f"El resultado de la multiplicación es: {resultado}")
