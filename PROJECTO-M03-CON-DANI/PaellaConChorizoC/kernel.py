import os
import logging
from collections import defaultdict

# Configuración del logging
LOG_DIR = os.path.join(".", "log")
INPUT_DIR = os.path.join(".", "entrada")
OUTPUT_DIR = os.path.join(".", "sortida")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'paraules.log'),
    filemode='a',
    level=logging.DEBUG,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Nombres de los archivos
FILE_OUT_ING = os.path.join(OUTPUT_DIR, 'words-ing.txt')
FILE_OUT_ITB = os.path.join(OUTPUT_DIR, 'words-itb.txt')
FILE_OUT_TIC = os.path.join(OUTPUT_DIR, 'words-tic.txt')
FILE_OUT_TICA = os.path.join(OUTPUT_DIR, 'words-tica.txt')
FILE_OUT_CIO = os.path.join(OUTPUT_DIR, 'words-cio.txt')
FILE_IN = os.path.join(INPUT_DIR, 'paraules.txt')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'contarPrimeraLetra.txt')


def read_words_from_file():
    if not os.path.exists(INPUT_DIR):
        logging.error(f"El directorio de entrada {INPUT_DIR} no existe")
        return None
    try:
        with open(FILE_IN, mode="r", encoding="utf-8") as f:
            words = [line.strip() for line in f]
        logging.info(f"Archivo leido correctamente")
        return words
    except:
        logging.error("el archivo no se ha abierto")
        return None


def write_to_file(filename, words):
    if not os.path.exists(OUTPUT_DIR):
        logging.error(f"El directorio de salida {OUTPUT_DIR} no existe")
        return
    """Escribe una lista de palabras en un archivo"""
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            for word in words:
                f.write(word + '\n')
        logging.info(f"{len(words)} palabras escritas en {filename}")
    except Exception as e:
        logging.error(f"Error al escribir en {filename}: {str(e)}")


def process_words(words):
    """Procesa una lista de palabras y las escribe en los archivos correspondientes"""
    words_ing = [word for word in words if word.endswith('ing')]
    words_itb = [word for word in words if word.endswith('itb')]
    words_tic = [word for word in words if word.endswith('tic')]
    words_tica = [word for word in words if word.endswith('tica')]
    words_cio = [word for word in words if word.endswith('cio')]

    write_to_file(FILE_OUT_ING, words_ing)
    write_to_file(FILE_OUT_ITB, words_itb)
    write_to_file(FILE_OUT_TIC, words_tic)
    write_to_file(FILE_OUT_TICA, words_tica)
    write_to_file(FILE_OUT_CIO, words_cio)


def write_letter_counts_to_file(words):
    try:
        counts = {}
        for word in words:
            if word:  # check if word is not empty
                if word[0].lower() in counts:
                    counts[word[0].lower()] += 1
                else:
                    counts[word[0].lower()] = 1

        with open(OUTPUT_FILE, 'w') as f:
            for letter, count in sorted(counts.items()):
                f.write(f'{count}\t{letter}\n')

        logging.info(f"Archivo escrito correctamente")
    except:
        logging.error("No se ha podido escribir en el archivo de salida", OUTPUT_FILE)
        return None
