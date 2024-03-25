from functools import reduce

def encontrar_maximo(lista: list[int]) -> int:
    """
    Función que encuentra el máximo valor en una lista de números.

    Parámetros:
        lista (list): La lista de números en la cual se buscará el máximo.

    Retorna:
        int: El valor máximo en la lista.
    """

    maximo = lista[0]
    for x in lista:
        if (x > maximo):
            maximo = x
    return maximo

def encontrar_minimo(lista: list[int]) -> int:
    """
    Función que encuentra el mínimo valor en una lista de números.

    Parámetros:
        lista (list): La lista de números en la cual se buscará el mínimo.

    Retorna:
        int: El valor mínimo en la lista.
    """
    
    minimo = lista[0]
    for x in lista:
        if (x < minimo):
            minimo = x
    return minimo

if (__name__ == "__main__"):
    numeros = [1, 2, 3, 4, 5]
    # numeros = [10, 5, 20, 8, 15]

    print(f"El número máximo en la lista es: {encontrar_maximo(numeros)} y el minimo es: {encontrar_minimo(numeros)}")