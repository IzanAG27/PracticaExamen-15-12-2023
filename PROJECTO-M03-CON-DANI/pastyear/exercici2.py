#Aqui preguntem per la ruta
def Preguntar_Ruta():
    ruta = str(input("Quina es la ruta al arxiu a editar?:"))
    return ruta


#Aqui escrivim el fitxer
def Escriure_Fitxer(ruta):
    with open(ruta, mode="rt", encoding="utf-8") as original, open('./fitxersA/ocells_2.txt', mode='wt',
                                                                   encoding="utf-8") as resultat:
        for line in original:
            line = line.replace('3', '-')
            line = line.replace('6', '*')
            line = line.replace('*', '6', 1)
            resultat.write(line)


Escriure_Fitxer(Preguntar_Ruta())
