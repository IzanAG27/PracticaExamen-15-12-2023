def mcd_no_recursivo(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcd_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mcd_recursivo(b, a % b)