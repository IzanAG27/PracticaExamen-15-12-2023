"""
    Autores: Daniel Arco, Izan Arnaiz.
    Fecha: 05/05/2024
    Curso: 2023/2024
    Grupo: ASIXc1A
    Entrega: Pt3.1
    Descripción:

    El trabajo consiste en integrar las tareas previas y
    trabajar con archivos. El programa debe leer desde "paraules.txt"
    y escribir la salida en "paraules_boges.txt". También debe implementar
    un registro de errores llamado "boges.log", que registra información
    importante como el inicio, fin y errores durante la ejecución.
    El programa no tendrá un menú interactivo y los resultados se guardarán
    en archivos o en el registro de errores. Este último debe mantener
    un historial de todas las ejecuciones del programa.

"""

# region Importación de librerías
import requests
import re
import time
import logging
from colorama import *
import random

# endregion

# region Variables globales
INPUT_FILE = "25 MANERAS DE GANARSE A LA GENTE - .txt"
OUTPUT_FILE = "paraules_boges.txt"
# endregion

# region Configuración de logging
logging.basicConfig(
    filename='boges.log',
    filemode='a',
    level=logging.DEBUG,
    encoding='utf-8',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


# endregion

# region Funciones
def get_data_from_file(INPUT_FILE):
    try:
        logging.info("Comenzando proceso de lectura.")
        with open(INPUT_FILE, "rt", encoding="UTF-8") as f:
            text = f.read()
            logging.info("Archivo leído correctamente.")
            if len(text) > 3:
                time.sleep(2)
                text = desordenar_text(text)
                return text, 1
            else:
                logging.warning("El texto es demasiado corto, puede que no se desordene correctamente.")
                return None, 0
    except FileNotFoundError as e:
        logging.error("Error al abrir el archivo %s: %s", INPUT_FILE, str(e))
        return None, -1
    except PermissionError as e:
        logging.error("Error: %s", str(e))
        return None, -1
    except UnicodeDecodeError as e:
        logging.error("Error: %s", str(e))
        return None, -1
    except Exception as e:
        logging.error("Error: %s", str(e))
        return None, -1


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
    palabras = dividir_Palabras(text, urls)  # Pass urls to the function


def write_ranzomized_output(text_randomizada, code):
    if code == 1:
        logging.info("Comenzando proceso de escritura.")
        with open(OUTPUT_FILE, "wt", encoding="UTF-8") as OUTPUT:
            OUTPUT.write(text_randomizada)
            logging.info("Archivo escrito correctamente.")
    else:
        logging.error("Error: No se ha podido escribir el fichero, intentalo nuevamente...")
# endregion
