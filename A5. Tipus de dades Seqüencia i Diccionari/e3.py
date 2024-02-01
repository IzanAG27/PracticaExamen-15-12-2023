# Inicialitza una llista per emmagatzemar les notes
notes = []

# Llegeix les 5 notes per teclat (validant que estiguin entre 0 i 10)
for x in range(5):
    nota = float(input("Introdueix una nota (entre 0 i 10): "))
    while nota < 0 or nota > 10:
        print("La nota ha de ser entre 0 i 10. Torna a intentar-ho.")
        nota = float(input("Introdueix una nota (entre 0 i 10): "))
    notes.append(nota)

# Mostra totes les notes
print("Notes:", notes)

# Calcula la mitjana
mitjana = sum(notes) / len(notes)
print(f"Mitjana: {mitjana:.2f}")

# Mostra la nota més alta i la més baixa
nota_mes_alta = max(notes)
nota_mes_baixa = min(notes)
print(f"Nota més alta: {nota_mes_alta}")
print(f"Nota més baixa: {nota_mes_baixa}")
