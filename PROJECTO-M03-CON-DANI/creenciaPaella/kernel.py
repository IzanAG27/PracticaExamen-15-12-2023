import os
import logging

# Configuración del logging
LOG_DIR = os.path.join(".", "log")
INPUT_DIR = os.path.join(".", "entrada")
OUTPUT_DIR = os.path.join(".", "sortida")


logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'paraules.log'),
    filemode='a',
    level=logging.DEBUG,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Nombres de los archivos
FILE_OUT_ING = os.path.join(OUTPUT_DIR, 'words-ing.txt')
FILE_OUT_TIC = os.path.join(OUTPUT_DIR, 'words-tic.txt')
FILE_OUT_TICA = os.path.join(OUTPUT_DIR, 'words-tica.txt')
FILE_OUT_CIO = os.path.join(OUTPUT_DIR, 'words-cio.txt')
FILE_OUT_AC = os.path.join(OUTPUT_DIR, 'words-ac.txt')
FILE_IN = os.path.join(INPUT_DIR, 'paraules.txt')


def read_from_file(filename):
    """Lee una lista de palabras de un archivo"""
    words = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                words.append(line.strip())
        logging.info(f"{len(words)} palabras leídas de {filename}")
    except Exception as e:
        logging.error(f"Error al leer de {filename}: {str(e)}")
    return words


def process_words(words):
    """Procesa una lista de palabras y las escribe en los archivos correspondientes"""
    words_ing = [word for word in words if word.startswith('ing')]
    words_tic = [word for word in words if word.startswith('tic')]
    words_tica = [word for word in words if word.startswith('tica')]
    words_cio = [word for word in words if word.startswith('cio')]
    words_ac = [word for word in words if word.startswith('ac')]

    write_to_file(FILE_OUT_ING, words_ing)
    write_to_file(FILE_OUT_TIC, words_tic)
    write_to_file(FILE_OUT_TICA, words_tica)
    write_to_file(FILE_OUT_CIO, words_cio)
    write_to_file(FILE_OUT_AC, words_ac)


def write_to_file(filename, words):
    """Escribe una lista de palabras en un archivo"""
    try:
        with open(filename, 'w') as f:
            for word in words:
                f.write(word + '\n')
        logging.info(f"{len(words)} palabras escritas en {filename}")
    except Exception as e:
        logging.error(f"Error al escribir en {filename}: {str(e)}")









