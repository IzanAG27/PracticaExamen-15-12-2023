path = "./fitxersA/paraules.txt"


#Aqui guardarem totes les paraules que hi han per linia
def ContarLletresPerLinia(path):
    lletresPerLinia = []
    with open(path, mode='rt', encoding='utf-8') as fitxer:
        for i, line in enumerate(fitxer):
            lletresPerLinia.append(len(line))
    return lletresPerLinia


#Aqui guardarem el numero total de lletres que hi ha en el fitxer
def ContarLletresTotal(path):
    lletres = 0
    saltsDeLinia = 0
    with open(path, mode='rt', encoding='utf-8') as fitxer:
        for i, line in enumerate(fitxer):
            lletres = lletres + (len(line))
    for x in range(len(ContarLletresPerLinia(path))):
        saltsDeLinia = saltsDeLinia + 1
    return lletres - saltsDeLinia


#Aqui guardem el contingut de les linias
def AgafarLinias(path):
    Linias = []
    with open(path, mode='rt', encoding='utf-8') as fitxer:
        for i, line in enumerate(fitxer):
            Linias.append(line)
    return Linias


#Aqui esrcrivim tota la informacio que hem agafat anteriorment
def Escriure():
    with open('./fitxersA/paraules' + str(ContarLletresTotal(path)) + '.txt', mode='wt', encoding="utf-8") as paraules:
        for i in range(len(AgafarLinias(path))):
            paraules.write(str(ContarLletresPerLinia(path)[i] - 1))
            paraules.write("    ")
            paraules.write(AgafarLinias(path)[i])


Escriure()
