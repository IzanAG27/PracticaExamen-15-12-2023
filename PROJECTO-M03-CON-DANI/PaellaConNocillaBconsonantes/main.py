from kernel import *


def main():
    if not os.path.exists(INPUT_DIR):
        logging.error(f"El directorio de entrada {INPUT_DIR} no existe.")
        return
    if not os.path.exists(OUTPUT_DIR):
        logging.error(f"El directorio de salida {OUTPUT_DIR} no existe.")
        return

    words = leer_archivo('paraules.txt')
    escribir_palabras_por_longitud(words)
    escribir_palabras_con_consonantes(words)


if __name__ == "__main__":
    main()
