def ordenamiento_burbuja(lista):
    """
    Función que ordena una lista de números utilizando el algoritmo de ordenamiento burbuja.

    Parámetros:
        lista (list): La lista de números que se ordenará.

    Retorna:
        None: La lista se ordena in-place, por lo que no es necesario devolver nada.
    """
    
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

if (__name__ == "__main__"):
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", numeros)

    ordenamiento_burbuja(numeros)

    print("Lista ordenada:", numeros)
