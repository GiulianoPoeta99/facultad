def producto_punto(vec1: list[int], vec2: list[int]) -> int:
    """
    Función que calcula el producto punto entre dos vectores.

    Parámetros:
        vec1 (list): El primer vector.
        vec2 (list): El segundo vector.

    Retorna:
        float: El producto punto entre los dos vectores.
    """

    return sum(x * y for x, y in zip(vector1, vector2))

if (__name__ == "__main__"):
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    print("El producto punto de los vectores es: ", producto_punto(vector1, vector2))
