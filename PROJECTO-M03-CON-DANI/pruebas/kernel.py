"""
Descripción:
Crea un directorio de entrada y uno de salida. Si estos directorios no existen, el programa debería crearlos automáticamente.
En el directorio de entrada, coloca un archivo de texto con varias líneas de texto.
El programa debe leer el archivo de entrada, línea por línea.
Para cada línea leída, el programa debe contar el número de caracteres en esa línea.
El programa debe escribir en un archivo de salida el número de caracteres de cada línea del archivo de entrada. Cada línea en el archivo de salida debe corresponder a una línea en el archivo de entrada.
Finalmente, el programa debe escribir en el archivo de salida el número total de caracteres en el archivo de entrada.
"""
import os

INPUT_DIR = os.path.join(".", "entrada")
OUTPUT_DIR = os.path.join(".", "salida")
INPUT_FILE = os.path.join(INPUT_DIR, "paraules.txt")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "sortida.txt")


if not os.path.exists(INPUT_FILE):
    with open(INPUT_FILE, 'w') as file:
        pass




def escribir_caracteres(INPUT_FILE, OUTPUT_FILE):
    with open(INPUT_FILE, 'r') as in_file, open(OUTPUT_FILE, 'w') as out_file:
        for line in in_file:
            char_count = len(line)
            out_file.write(f"{char_count}\n")

escribir_caracteres(INPUT_FILE, OUTPUT_FILE)

