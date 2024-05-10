"""
    Noms: Daniel Arco, Izan Arnaiz.
    Data: 20/03/2024
    Grup: ASIXc1A
    Descripció:
    Módul per a la execució de main.
"""

import crazy_words as c


if __name__ == "__main__":
    frase = c.menu()
    frase, urls = c.ignorar_urls(frase)
    palabras = c.dividir_Palabras(frase, urls)
    palabras_desordenadas = [c.desordenar_palabras(palabra) for palabra in palabras]
    frase_desordenada = c.reconstruir_sentencia(palabras_desordenadas, urls)
    print(frase_desordenada)


