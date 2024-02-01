# Solicitar un número al usuario
numero = int(input("Introduce un número: "))

# Crear una lista de strings representando los pares clave-valor
pares_clave_valor = [f"{{{i}:{i**2}}}" for i in range(1, numero + 1)]

# Mostrar la lista como una cadena
resultado = ",".join(pares_clave_valor)
print(resultado)
