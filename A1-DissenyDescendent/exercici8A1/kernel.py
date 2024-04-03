def factorial_no_recursivo(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
