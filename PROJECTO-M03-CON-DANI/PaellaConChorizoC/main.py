from kernel import *


def main():
    if not os.path.exists(INPUT_DIR):
        logging.error(f"El directorio de entrada {INPUT_DIR} no existe.")
        return
    if not os.path.exists(OUTPUT_DIR):
        logging.error(f"El directorio de salida {OUTPUT_DIR} no existe.")
        return
    words = read_words_from_file()
    if words is not None:
        process_words(words)
        write_letter_counts_to_file(words)
    logging.info(f"La ejecucion de la tarea ha sido un exito")


if __name__ == "__main__":
    main()
