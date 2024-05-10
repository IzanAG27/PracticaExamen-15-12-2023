"""
    Autores: Daniel Arco, Izan Arnaiz.
    Fecha: 05/05/2024
    Curso: 2023/2024
    Grupo: ASIXc1A
    Entrega: Pt3.2
    Descripción:

    Aquesta versió haurà de processar tots els arxius,
    amb extensió txt del directori d'entrada.
    Haurà de generar un fitxer de _sortida per a cada
    un dels que trobi a l’entrada amb el mateix nom,
    afegint “_boges”. I evidentment, processat ;-)

"""

# region Imports
from kernel import *
import os
import logging


# endregion

# region Main
def main():
    if not os.path.exists(INPUT_DIR):
        logging.error("El directorio de entrada %s no se encuentra", INPUT_DIR)
        return

    for file_name in os.listdir(INPUT_DIR):
        if file_name.endswith(".txt"):
            input_file = os.path.join(INPUT_DIR, file_name)
            output_file = os.path.join(OUTPUT_DIR, file_name.replace(".txt", "_boges.txt"))
            text, code = get_data_from_file(input_file)
            text, urls = ignorar_urls(text)
            palabras = dividir_Palabras(text, urls)
            palabras_desordenadas = [desordenar_palabras(palabra) for palabra in palabras]
            text_randomizada = reconstruir_sentencia(palabras_desordenadas, urls)
            write_ranzomized_output(output_file, text_randomizada, code)


if __name__ == "__main__":
    main()
# endregion