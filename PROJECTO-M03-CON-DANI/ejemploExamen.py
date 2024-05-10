import logging

# Configuración del logging
logging.basicConfig(filename='programa.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# Función 1
def funcion1():
    """
    Esta es la función 1. Realiza la tarea X.
    """
    try:
        # Código de la función 1
        pass
    except Exception as e:
        logging.error(f"Error en la función 1: {str(e)}")

# Función 2
def funcion2():
    """
    Esta es la función 2. Realiza la tarea Y.
    """
    try:
        # Código de la función 2
        pass
    except Exception as e:
        logging.error(f"Error en la función 2: {str(e)}")

# Función principal
def main():
    """
    Esta es la función principal. Llama a las otras funciones y maneja las excepciones.
    """
    try:
        funcion1()
        funcion2()
    except Exception as e:
        logging.error(f"Error en la función main: {str(e)}")

if __name__ == "__main__":
    main()