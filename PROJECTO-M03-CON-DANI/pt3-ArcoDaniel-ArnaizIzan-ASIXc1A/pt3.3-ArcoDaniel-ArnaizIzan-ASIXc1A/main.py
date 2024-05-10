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

# region imports
from kernel import *
import os
import time
import logging


# endregion

# region main
def main():
    if not os.path.exists(INPUT_DIR):
        logging.error("El directorio de entrada %s no se encuentra", INPUT_DIR)
        return
    tiempo_inicio = time.time()
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

    tiempo_total = time.time() - tiempo_inicio

    dias, resto = divmod(tiempo_total, 86400)
    horas, resto = divmod(resto, 3600)
    minutos, segundos = divmod(resto, 60)
    milisegundos = (tiempo_total - int(tiempo_total)) * 1000

    logging.info("Tiempo total transcurrido en procesar todos los archivos: %02d días, %02d horas, %02d minutos, %02d "
                 "segundos, %03d milisegundos." % (
                     dias, horas, minutos, segundos, int(milisegundos)))


if __name__ == "__main__":
    main()
# endregion
