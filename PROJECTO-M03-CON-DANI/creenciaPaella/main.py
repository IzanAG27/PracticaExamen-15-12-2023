from kernel import *


def main():
    if not os.path.exists(INPUT_DIR):
        logging.error(f"El directorio de entrada {INPUT_DIR} no existe.")
        return
    if not os.path.exists(OUTPUT_DIR):
        logging.error(f"El directorio de salida {OUTPUT_DIR} no existe.")
        return
    """Función principal que coordina la lectura, procesamiento y escritura de palabras"""
    words = read_from_file(FILE_IN)
    process_words(words)


if __name__ == "__main__":
    main()
