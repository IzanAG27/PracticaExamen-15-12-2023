# Inicializa una lista para almacenar las temperaturas de cada día
temperaturas = []

# Pide la temperatura mínima y máxima de cada uno de los 5 días
for dia in range(1, 6):
    temperatura_minima = float(input(f"Introduce la temperatura mínima para el día {dia}: "))
    temperatura_maxima = float(input(f"Introduce la temperatura máxima para el día {dia}: "))
    temperaturas.append([temperatura_minima, temperatura_maxima])

# Muestra la temperatura media de cada día
print("\nTemperatura media de cada día:")
for dia, temperatura in enumerate(temperaturas, 1):
    temperatura_media = sum(temperatura) / 2
    print(f"Día {dia}: {temperatura_media:.2f} grados Celsius")

# Muestra los días con menos temperatura
temperatura_minima_promedio = min([sum(temperatura) / 2 for temperatura in temperaturas])
print(f"\nDías con menos temperatura ({temperatura_minima_promedio:.2f} grados Celsius):")
for dia, temperatura in enumerate(temperaturas, 1):
    temperatura_media = sum(temperatura) / 2
    if temperatura_media == temperatura_minima_promedio:
        print(f"Día {dia}")

# Pide una temperatura por teclado y muestra los días con esa temperatura máxima
temperatura_busqueda = float(input("\nIntroduce una temperatura para buscar los días con esa temperatura máxima: "))
dias_coincidentes = [dia + 1 for dia, temperatura in enumerate(temperaturas) if temperatura[1] == temperatura_busqueda]

if dias_coincidentes:
    print(f"\nDías con temperatura máxima de {temperatura_busqueda} grados Celsius: {', '.join(map(str, dias_coincidentes))}")
else:
    print(f"No hay días con temperatura máxima de {temperatura_busqueda} grados Celsius.")
