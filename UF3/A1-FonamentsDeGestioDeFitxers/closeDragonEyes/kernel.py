file_text = "dragon.in"
out_file = "dragon.out"

fEntrada = open(file_text, mode="rt", encoding="UTF-8")
contenido = fEntrada.read()
contenidoModificado = contenido.replace("0", "X")

fSortida = open(out_file, mode="wt", encoding="UTF-8")
fSortida.write(contenido.replace("0", "X"))
fSortida.close()
