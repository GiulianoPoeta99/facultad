def interseccion(lista1: list[int], lista2: list[int]) -> list[int]:
    """
    Función que encuentra la intersección entre dos listas de números y devuelve una lista con los elementos comunes.

    Parámetros:
        lista1 (list[int]): La primera lista de números.
        lista2 (list[int]): La segunda lista de números.

    Retorna:
        list[int]: Una lista con los elementos comunes entre las dos listas.
    """
    return list(set(lista1).intersection(set(lista2)))

if (__name__ == "__main__"):
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [1, 3, 5, 7, 9]

    print("Los elementos comunes son de las listas son: ", interseccion(lista1, lista2))