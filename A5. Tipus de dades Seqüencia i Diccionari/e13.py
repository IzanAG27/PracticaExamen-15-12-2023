# Inicializa las listas para almacenar los nombres y los kilómetros
noms = []
kms = []

# Solicita los nombres de los conductores
num_conductors = int(input("Introduce el número de conductores: "))
for x in range(num_conductors):
    nom = input("Introduce el nombre del conductor: ")
    noms.append(nom)

# Solicita los kilómetros para cada conductor en una sola entrada
for i in range(num_conductors):
    kms_conductor = [float(x) for x in input(f"Introduce los kilómetros para {noms[i]} separados por comas: ").split(',')]
    kms.append(kms_conductor)

# Calcula los kilómetros totales por conductor
total_kms = [sum(kms_conductor) for kms_conductor in kms]

# Muestra la lista con los nombres de los conductores y los kilómetros totales semanales
print("\nResumen de kilómetros semanales:")
for i in range(num_conductors):
    print(f"{noms[i]} - Total Kilómetros: {total_kms[i]:.2f}")
