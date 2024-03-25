def ordenar_claves(diccionario: dict) -> list[str]:
    """
    Función que ordena alfabéticamente las claves de un diccionario y las devuelve en una lista.

    Parámetros:
        diccionario (dict): El diccionario del cual se ordenarán las claves.

    Retorna:
        list[str]: Una lista de las claves del diccionario ordenadas alfabéticamente.
    """
    
    return sorted(diccionario.keys())

if (__name__ == "__main__"):
    diccionario = {
        "b": 2, 
        "c": 3, 
        "a": 1
    }

    print("Claves ordenadas alfabéticamente: ", ordenar_claves(diccionario))