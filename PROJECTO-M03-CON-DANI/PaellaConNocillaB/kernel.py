import os
import logging

# Configuración del logging
LOG_DIR = os.path.join(".", "log")
INPUT_DIR = os.path.join(".", "entrada")
OUTPUT_DIR = os.path.join(".", "_sortida")
LOG_FILE = os.path.join(LOG_DIR, 'programa.log')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
if not os.path.exists(INPUT_DIR):
    os.makedirs(INPUT_DIR)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

logging.basicConfig(filename=LOG_FILE,
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def leer_archivo(filename):
    logging.info(f"Leyendo el archivo {filename}...")
    with open(os.path.join(INPUT_DIR, filename), 'r', encoding='utf-8', errors='ignore') as f:
        words = [word.strip() for word in f]
    return words


def escribir_palabras_por_longitud(words):
    for word in words:
        length = len(word)
        if length in [2, 4, 6, 8, 10]:
            with open(os.path.join(OUTPUT_DIR, f'paraules-{length}.txt'), 'a', encoding='utf-8') as f:
                f.write(word + '\n')
    logging.info(f"Las palabras del fichero de entrada 'paraules.txt' se han escrito en el archivo correspondiente.")
    logging.info("Se ha terminado de escribir en el archivo correspondiente.")


def contar_vocales(word):
    return sum(1 for char in word if char.lower() in 'aeiou')


def escribir_palabras_con_vocales(words):
    with open(os.path.join(OUTPUT_DIR, 'vocales.txt'), 'w', encoding='utf-8') as f:
        for word in words:
            vocales = ''.join([char for char in word if char.lower() in 'aáàéèìíòóúùeiou'])
            f.write(f"{vocales}\t{word}\n")
    logging.info("Las palabras del fichero de entrada 'paraules.txt' se han escrito en el archivo 'vocales.txt'.")
    logging.info("Se ha terminado de escribir en el archivo 'vocales.txt'.")



