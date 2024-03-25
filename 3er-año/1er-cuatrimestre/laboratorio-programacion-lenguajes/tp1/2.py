def fibonacci(n: int) -> list[int]:
    """
    Función que genera los primeros n términos de la serie de Fibonacci.

    Parámetros:
        n (int): El número de términos de la serie de Fibonacci que se desea generar.

    Retorna:
        list: Una lista que contiene los primeros n términos de la serie de Fibonacci.
    """

    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])
    return fib_sequence[:n]

    # fib_sequence = [0, 1]   
    # reduce(lambda x, _: fib_sequence.append(sum(fib_sequence[-2:])), range(2, n), None)
    # return fib_sequence[:n]


if (__name__ == "__main__"):
    n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci que desea generar: "))

    print(f"Los primeros {n} términos de la serie de Fibonacci son: ", fibonacci(n))