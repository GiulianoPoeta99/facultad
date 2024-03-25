def claves_comunes(lista: list[dict]) -> list[str]:
    """
    Función que encuentra las claves comunes entre los diccionarios de una lista y devuelve una lista con esas claves.

    Parámetros:
        lista (list[dict]): La lista de diccionarios a analizar.

    Retorna:
        list[str]: Una lista con las claves comunes entre todos los diccionarios de la lista.
    """
    
    claves = set(lista[0].keys())

    for diccionario in lista[1:]:
        claves = claves.intersection(diccionario.keys())

    return list(claves) 

if (__name__ == "__main__"):
    lista = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 4, 'b': 5, 'd': 6},
        {'a': 7, 'b': 8, 'c': 9},
    ]

    print(claves_comunes(lista)) 