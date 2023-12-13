

# comprobar = True
# while comprobar == True:
#     n = int(input(""))
#     if n > 0:
#         comprobar = False
#         for i in range (1, n + 1):
#             for x in range (1, i + 1):
#                 print(x, end=" ")
#             print("")
#
#         for i in range (n-1, 0, -1):
#             for x in range (1, i + 1):
#                 print(x, end=" ")
#             print("")
#     else:
#         print("El número debe ser positivo")
n = int(input(""))
for i in range(1, n + 1):
    for x in range(1, i + 1):
        print(x, end=" ")
    print("")
for i in range(n - 1, 0, -1):
    for x in range(1, i + 1):
        print(x, end=" ")
    print("")

