# Llista amb el nombre de dies de cada mes (suposant que febrer sempre té 28 dies)
dies_mesos = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes_valid = False

while not mes_valid:
    # Llegeix un número de mes de l'usuari
    mes = int(input("Introdueix un número de mes (entre 1 i 12): "))

    # Validació del nombre de mes
    if 1 <= mes <= 12:
        mes_valid = True
    else:
        print("Error: Introdueix un número de mes vàlid (entre 1 i 12).")

# Obté el nombre de dies i el nom del mes
nombre_dies = dies_mesos[mes]
noms_mesos = [
    "Gener", "Febrer", "Març", "Abril", "Maig", "Juny",
    "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre"
]
nom_mes = noms_mesos[mes]

# Mostra el nombre de dies i el nom del mes
print(f"El mes de {nom_mes} té {nombre_dies} dies.")
