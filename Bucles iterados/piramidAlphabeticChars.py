"""
Imprimir de la A fins la Z.
A cada linia apareix un carcater i la seguent linia apareix un carcater més de forma progresiva. Fins aconseguir tenir una linia que mostri de la A fins la Z
Output
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
A B C D E F G H
A B C D E F G H I
A B C D E F G H I J
"""

n = int(input(""))


for x in range (1, n + 1):
    print("")
    for x in range (1, x + 1):
        print()