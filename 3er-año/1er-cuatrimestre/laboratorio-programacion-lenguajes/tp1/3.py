def factorial(n: int) -> int:
    """
    Función que calcula el factorial de un número dado.

    Parámetros:
        n (int): El número entero del cual se calculará el factorial.

    Retorna:
        int: El factorial del número n.
    """

    # if ((n == 0) | (n == 1)):
    #     return 1
    # else:
    #     return n * factorial(n - 1)
    
    return 1 if ((n == 0) | (n == 1)) else (n * factorial(n - 1))

if (__name__ == "__main__"):
    n = 5
    print(f"El factorial de {n} es: ", factorial(n))