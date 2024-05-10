"""
    Autor: Izan Arnaiz.
    Fecha: 09/05/2024
    Curso: 2023/2024
    Grupo: ASIXc1A
    Entrega: Examen UF3
    Descripción:
    Fichero main que ejecuta el programa de paraules.txt.
"""
import logging

# region imports
from kernel import *


# endregion

# region main
def main():
    try:
        if not os.path.exists(INPUT_DIR):
            logging.error("El directorio de entrada %s no se encuentra", INPUT_DIR)
            return
        if not os.path.exists(OUTPUT_DIR):
            logging.error("El directorio de salida %s no se encuentra", OUTPUT_DIR)
            return
        logging.info(f"Comenzando la lectura del archivo {INPUT_FILE}...")
        words = read_file_to_get_words()
        if words is not None:
            process_words(words)
            count_chars_and_write_file(words)
        logging.info(f"La ejecucion del programa ha sido un éxito.")
        logging.info("-------------------------------------------------------------------------")
    except ValueError:
        logging.error("Error en la ejecución del programa, por favor verifica los archivos de registro.")


if __name__ == "__main__":
    main()
# endregion
