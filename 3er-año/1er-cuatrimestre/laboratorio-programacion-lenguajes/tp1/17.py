def impares_cuadrados(lista: list[int]) -> list[int]:
    """
    Función que toma una lista de números como entrada y devuelve una lista con los cuadrados de los números impares de la lista.

    Parámetros:
        lista (list[int]): La lista de números a analizar.

    Retorna:
        list[int]: Una lista con los cuadrados de los números impares de la lista.
    """
    return [x**2 for x in lista if ((x % 2) != 0)]

if (__name__ == "__main__"):
    numeros = [1, 2, 3, 4, 5]
    print(f"Los numero impares al cuadrado son: ", impares_cuadrados(numeros))