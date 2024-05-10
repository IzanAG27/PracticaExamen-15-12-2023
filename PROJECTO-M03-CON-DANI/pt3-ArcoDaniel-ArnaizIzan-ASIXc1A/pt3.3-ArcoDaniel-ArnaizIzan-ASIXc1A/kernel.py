"""
    Autores: Daniel Arco, Izan Arnaiz.
    Fecha: 05/05/2024
    Curso: 2023/2024
    Grupo: ASIXc1A
    Entrega: Pt3.3
    Descripción:

    Aquesta versió haurà de mostrar
    el temps transcorregut en processar els arxius
    amb format (DD:HH:MM:SS:MS).

"""

# region Imports
import os

import re
import time
import logging
import random
import sys

# endregion

# region Variables globales
INPUT_DIR = os.path.join(".", "entrada")
OUTPUT_DIR = os.path.join(".", "_sortida")
LOG_DIR = os.path.join(".", "log")
# endregion

# region Configuración de logging
logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'boges.log'),
    filemode='a',
    level=logging.DEBUG,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# endregion

# region Funciones
def get_data_from_file(file_path):
    try:
        logging.info("Comenzando proceso de lectura del archivo '%s'.", file_path)
        try:
            with open(file_path, "rt", encoding="utf-8") as f:
                text = f.read()
        except UnicodeDecodeError as e:
            logging.error("El archivo '%s' no está en formato UTF-8 y no puede ser leído.", file_path)
            return None, -2
        except FileNotFoundError as e:
            logging.error("Error al abrir el archivo '%s'", file_path)
            return None, -1
        logging.info("Archivo '%s' leído correctamente.", file_path)
        if len(text) > 3:
            time.sleep(2)
            text = desordenar_text(text)
            return text, 1
        else:
            logging.warning("El texto es demasiado corto, puede que no se desordene correctamente.")
            return None, 0
    except Exception as e:
        logging.error("Error desconocido al procesar el archivo '%s: %s'", file_path, str(e))
        return None, -3


def ignorar_urls(text):
    if not isinstance(text, str):
        text = str(text)
    urls = re.findall(r'(http://|https://|ssh@)[^\s]+', text)
    for i, url in enumerate(urls):
        text = text.replace(url, f'URLPLACEHOLDER{i}')
    return text, urls


def dividir_Palabras(text, urls):
    return re.split('([^a-zA-Z0-9áéíóúÁÉÍÓÚ])', text)


def desordenar_palabras(palabra):
    if 'URLPLACEHOLDER' in palabra or (palabra.isdigit() and len(palabra) == 9):
        return palabra
    elif len(palabra) > 3 and (palabra[0].isalnum() and palabra[-1].isalnum()):
        first_char = palabra[0]
        last_char = palabra[-1]
        centro = list(palabra[1:-1])
        random.shuffle(centro)
        return first_char + ''.join(centro) + last_char
    else:
        return palabra


def reconstruir_sentencia(resultado, urls):
    text_randomizada = ''.join(resultado)
    for i, url in enumerate(urls):
        text_randomizada = text_randomizada.replace(f'URLPLACEHOLDER{i}', url)
    return text_randomizada


def desordenar_text(text):
    text, urls = ignorar_urls(text)
    palabras = dividir_Palabras(text, urls)
    resultado = [desordenar_palabras(palabra) for palabra in palabras]
    return reconstruir_sentencia(resultado, urls)


def write_ranzomized_output(output_file, text_randomizada, code):
    if not os.path.exists(os.path.dirname(output_file)):
        logging.error("El directorio de salida '%s' no se encuentra", os.path.dirname(output_file))
        sys.exit()
    if code == 1:
        logging.info("Comenzando proceso de escritura del archivo '%s'.", output_file)
        with open(output_file, "wt", encoding="utf-8") as OUTPUT:
            OUTPUT.write(text_randomizada)
            logging.info("Archivo '%s' escrito correctamente.", output_file)
    else:
        logging.error("Error: No se ha podido escribir el archivo '%s', intentalo nuevamente...", output_file)
# endregion
