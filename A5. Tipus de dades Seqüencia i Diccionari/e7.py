# Declara tres llistes amb cinc sencers cadascuna
llista1 = []
llista2 = []
llista3 = []

# Demana valors per a llista1
print("Introdueix cinc valors per a llista1:")
for x in range(5):
    valor = int(input("Introdueix un valor: "))
    llista1.append(valor)

# Demana valors per a llista2
print("Introdueix cinc valors per a llista2:")
for x in range(5):
    valor = int(input("Introdueix un valor: "))
    llista2.append(valor)

# Omple llista3 amb la suma dels elements de llista1 i llista2
for i in range(5):
    suma = llista1[i] + llista2[i]
    llista3.append(suma)

# Mostra les llistes
print("llista1:", llista1)
print("llista2:", llista2)
print("llista3:", llista3)
