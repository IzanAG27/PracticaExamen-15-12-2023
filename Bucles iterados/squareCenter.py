
#
# valores = input("").split()
# val1 = int(valores[0])
# val2 = int(valores[1])
#
#
#
#
# for i in range(1, val1):
#     print("🌳")
#     for j in range(1, val1):
#         print("🌳", end="")
#     print()

extern = int(input("Introdueix la mida dels costats quadrat extern: "))
intern = int(input("Introdueix la mida dels costats quadrat intern: "))

for i in range(extern):
    for j in range(extern):
        if i < intern // 2 or i >= extern - intern // 2 or j < intern // 2 or j >= extern - intern // 2:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()