from functools import reduce

def suma_enteros(n: int) -> int:
    """
    Función que calcula la suma de los enteros desde 1 hasta n.

    Parámetros:
        n (int): El número entero hasta el cual se realizará la suma.

    Retorna:
        int: La suma de los enteros desde 1 hasta n.
    """

    # suma = lambda x, y: x + y
    # numeros = list(range(1, n + 1))
    # resultado = reduce(suma, numeros)
    
    # return resultado
    return reduce(lambda x, y: x + y, list(range(1, n + 1)))

if (__name__ == "__main__"):
    n = 10
    print("La suma de los enteros desde 1 hasta", n, "es:", suma_enteros(n))