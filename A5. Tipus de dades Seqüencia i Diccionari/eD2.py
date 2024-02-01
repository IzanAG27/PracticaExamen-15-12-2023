cadena = input("")

diccionari = {}

for caracter in cadena:
    if caracter.isalpha():
        if caracter in diccionari:
            diccionari[caracter] += 1
        else:
            diccionari[caracter] = 1
    elif caracter.isspace():
        if ' ' in diccionari:
            diccionari[' '] += 1
        else:
            diccionari[' '] = 1
    else:
        if caracter in diccionari:
            diccionari[caracter] += 1
        else:
            diccionari[caracter] = 1

# Mostrar el diccionari
for clau, valor in diccionari.items():
    print(f"{{{clau}:{valor}}}", end=', ')
