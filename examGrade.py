nota = float(input(""))

if nota < 5:
    print("Suspenso")
elif nota >= 5 and nota < 7:
    print("Suficiente")
elif nota >= 7 and nota < 9:
    print("Notable")
elif nota >= 9 and nota <= 10:
    print("Excelente")
else:
    print("Introduce bien los valores")
