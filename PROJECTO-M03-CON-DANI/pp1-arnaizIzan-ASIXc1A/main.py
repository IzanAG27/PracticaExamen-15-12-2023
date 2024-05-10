"""
    Autor: Izan Arnaiz.
    Fecha: 09/05/2024
    Curso: 2023/2024
    Grupo: ASIXc1A
    Entrega: Examen UF3
    Descripción:
    Fichero main que ejecuta el programa.
"""

# region imports
from kernel import *


# endregion

# region main
def main():
    if not os.path.exists(INPUT_DIR):
        logging.error("El directorio de entrada %s no se encuentra", INPUT_DIR)
        return
    if not os.path.exists(OUTPUT_DIR):
        logging.error("El directorio de salida %s no se encuentra", INPUT_DIR)
        return


if __name__ == "__main__":
    main()
# endregion
