def contar_numeros(lista: list[int]) -> dict:
    """
    Función que cuenta la cantidad de ocurrencias de cada número en una lista y devuelve un diccionario con los resultados.

    Parámetros:
        lista (list[int]): La lista de números a analizar.

    Retorna:
        dict: Un diccionario donde las claves son los números de la lista y los valores son la cantidad de ocurrencias de cada número.
    """
    
    contador = {}
    for numero in lista:
        if (numero in contador):
            contador[numero] += 1
        else:
            contador[numero] = 1
    return contador

if (__name__ == "__main__"):
    numeros = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]

    print("Diccionario de conteo de números:", contar_numeros(numeros))
