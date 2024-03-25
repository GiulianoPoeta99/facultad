from functools import reduce

def calcular_promedio(lista: list[int]) -> int:
    """
    Función que calcula el promedio de una lista de números.

    Parámetros:
        lista (list): La lista de números de la cual se calculará el promedio.

    Retorna:
        float: El promedio de los números en la lista.
    """
    
    # suma_total = reduce(lambda x, y: x + y, lista)
    # cantidad_numeros = len(lista)
    # return suma_total / cantidad_numeros

    return reduce(lambda x, y: x + y, lista) / len(lista)

if (__name__ == "__main__"):
    numeros = [1, 2, 3, 4, 5]
    print(f"El promedio de la lista {numeros} es: ", calcular_promedio(numeros))
