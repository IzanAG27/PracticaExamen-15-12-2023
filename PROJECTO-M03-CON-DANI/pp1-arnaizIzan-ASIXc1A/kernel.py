"""
    Autor: Izan Arnaiz.
    Fecha: 09/05/2024
    Curso: 2023/2024
    Grupo: ASIXc1A
    Entrega: Examen UF3

    Descripción:

    1ra parte: Programa que crea 5 ficheros con las palabras que comienzan por cada vocal de un fichero de entrada dado por el profesor.
    ejemplo:
    paraules-a.txt

    2nda parte: Crear una copia del fichero paraules.txt añadiendo un numero que indique la cantidad de caracteres de cada palabra.
    ejemplo:
    7   abporal
"""

# region imports
import logging
import os

# endregion

# region directorios
# Declaración de los directorios y ficheros de entrada y salida.
INPUT_DIR = os.path.join(".", "entrada")
OUTPUT_DIR = os.path.join(".", "sortida")
LOG_DIR = os.path.join(".", "log")

INPUT_FILE = os.path.join(INPUT_DIR, "paraules.txt")
OUTPUT_FILE_A = os.path.join(OUTPUT_DIR, "paraules-a.txt")
OUTPUT_FILE_E = os.path.join(OUTPUT_DIR, 'paraules-e.txt')
OUTPUT_FILE_I = os.path.join(OUTPUT_DIR, 'paraules-i.txt')
OUTPUT_FILE_O = os.path.join(OUTPUT_DIR, 'paraules-o.txt')
OUTPUT_FILE_U = os.path.join(OUTPUT_DIR, 'paraules-u.txt')
OUTPUT_FILE_QUANTITAT = os.path.join(OUTPUT_DIR, 'paraulesQuantitat.txt')
# endregion

# region configuracio_log
# Declaración de configuración del fichero de log.
logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'paraules.log'),
    filemode='a',
    level=logging.DEBUG,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# endregion

# region funciones
def read_file_to_get_words():
    # Tratamiento de error por si no existe el directorio de entrada.
    if not os.path.exists(INPUT_DIR):
        logging.error(f"El directorio de entrada {INPUT_DIR} no existe")
        return None
    try:
        with open(INPUT_FILE, mode="r", encoding="utf-8") as f:
            words = [line.strip() for line in f]
        logging.info(f"Archivo {INPUT_FILE} leido correctamente")
        return words
    except:
        logging.error(f"El archivo {INPUT_FILE} no se ha podido abrir.")
        return None


# region task1
def write_file_to_set_vowels(filename, words):
    if not os.path.exists(OUTPUT_DIR):
        logging.error(f"El directorio de salida {OUTPUT_DIR} no existe")
        return
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            for word in words:
                f.write(word + '\n')
        logging.info(f"{len(words)} palabras escritas en {filename}")
    except Exception as e:
        logging.error(f"Error al escribir en {filename}: {str(e)}")


def process_words(words):
    word_a = [word for word in words if word.startswith('a')]
    word_e = [word for word in words if word.startswith('e')]
    word_i = [word for word in words if word.startswith('i')]
    word_o = [word for word in words if word.startswith('o')]
    word_u = [word for word in words if word.startswith('u')]

    write_file_to_set_vowels(OUTPUT_FILE_A, word_a)
    write_file_to_set_vowels(OUTPUT_FILE_E, word_e)
    write_file_to_set_vowels(OUTPUT_FILE_I, word_i)
    write_file_to_set_vowels(OUTPUT_FILE_O, word_o)
    write_file_to_set_vowels(OUTPUT_FILE_U, word_u)


# endregion

# region task2
def count_chars_and_write_file(words):
    try:
        logging.info(f"Se va a comenzar a escribir el fichero {OUTPUT_FILE_QUANTITAT}.")
        for word in words:
            length = len(word)

            with open(os.path.join(OUTPUT_FILE_QUANTITAT), 'a', encoding='utf-8') as f:
                f.write(f"{length}\t{word}\n")
        logging.info(f"Fichero {OUTPUT_FILE_QUANTITAT} escrito correctamente.")

    except ValueError:
        logging.error("No se ha podido escribir en el archivo de salida", OUTPUT_FILE_QUANTITAT)
        return None
# endregion
# endregion
