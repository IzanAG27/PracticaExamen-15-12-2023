"""
    Autor: Izan Arnaiz.
    Fecha: 09/05/2024
    Curso: 2023/2024
    Grupo: ASIXc1A
    Entrega: Examen UF3
    Descripción:
    Programa que...
"""

# region imports
import logging
import os

# endregion

# region directorios
INPUT_DIR = os.path.join(".", "entrada")
OUTPUT_DIR = os.path.join(".", "sortida")
LOG_DIR = os.path.join(".", "log")
# Declarar aqui si hay varios INPUT_FILE
INPUT_FILE = os.path.join(INPUT_DIR, "paraules.txt")
# Declarar aquí si hay varios OUTPUT_FILE
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "outputfile.txt")
# endregion

# region configuracio_log
logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'boges.log'),
    filemode='a',
    level=logging.DEBUG,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# endregion

# region funciones
def leer_archivo():
    # Si no existe INPUT_DIR (error en log)
    if not os.path.exists(INPUT_DIR):
        logging.error(f"El directorio de entrada {INPUT_DIR} no existe")
        return None

    try:
        with open(INPUT_FILE, mode="r", encoding="utf-8") as f:
            file = f.read()  # Que quieres leer
        logging.info(f"Archivo leido correctamente")
        return file
    except FileNotFoundError:
        logging.error(f"El archivo {INPUT_FILE} no se ha encontrado.")
        return None


file = leer_archivo()


def escribir_archivo(file, words):
    # Si no existe OUTPUT_DIR (error en log)
    if not os.path.exists(OUTPUT_DIR):
        logging.error(f"El directorio de salida {OUTPUT_DIR} no existe")
        return

    try:
        with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:
            f.write("hola")
            # Que quieres escribir en el fichero (borrar f.write)
        logging.info(f" Archivo {OUTPUT_FILE} escrito correctamente.")
    except Exception as e:
        logging.error(f"Error al escribir en {OUTPUT_FILE}: {str(e)}")
# endregion
