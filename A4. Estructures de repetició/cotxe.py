# Solicitar la velocidad a través del teclado
velocidad = float(input("Introduce la velocidad de los coches (en km/h): "))

# Kilómetros iniciales donde se encuentran los coches
coche1_km = 70
coche2_km = 150

# Calcular la distancia relativa que se acortará cada hora
distancia_relativa_por_hora = velocidad * 2  # La suma de las velocidades de ambos coches

# Calcular la distancia inicial entre los coches
distancia_inicial = abs(coche1_km - coche2_km)

# Calcular en cuántas horas se encontrarán los coches
horas_para_encontrarse = distancia_inicial / distancia_relativa_por_hora

# Calcular en qué kilómetro se encontrarán
distancia_recorrida_por_cada_coche = velocidad * horas_para_encontrarse
kilometro_encuentro = coche1_km + distancia_recorrida_por_cada_coche

print(f"Los coches se encontrarán en el kilómetro {kilometro_encuentro:.2f}")
