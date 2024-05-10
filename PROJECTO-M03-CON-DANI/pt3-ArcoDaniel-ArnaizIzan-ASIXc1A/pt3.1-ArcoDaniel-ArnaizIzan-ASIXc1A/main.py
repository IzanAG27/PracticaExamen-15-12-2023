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

# region imports
from kernel import *
# endregion

# region main
def main():
    text, code = get_data_from_file(INPUT_FILE)
    text, urls = ignorar_urls(text)
    palabras = dividir_Palabras(text, urls)
    palabras_desordenadas = [desordenar_palabras(palabra) for palabra in palabras]
    text_randomizada = reconstruir_sentencia(palabras_desordenadas, urls)
    write_ranzomized_output(text_randomizada, code)


if __name__ == "__main__":
    main()
# endregion