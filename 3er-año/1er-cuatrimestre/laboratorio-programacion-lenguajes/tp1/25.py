def contar_letras(lista: list[str]) -> dict:
    """
    Función que cuenta la cantidad de veces que aparece cada letra en cada palabra de una lista, y devuelve un diccionario con los resultados.

    Parámetros:
        lista (list[str]): La lista de palabras a analizar.

    Retorna:
        dict: Un diccionario donde las claves son las palabras de la lista, y los valores son diccionarios que contienen la cantidad de veces que aparece cada letra en esa palabra.
    """
    
    contador = {}
    for palabra in lista:
        if (palabra not in contador):
            contador_letras = {}
            for letra in palabra:
                if (letra in contador_letras):
                    contador_letras[letra] += 1
                else:
                    contador_letras[letra] = 1
            contador[palabra] = {
                'cantidad': 1, 
                'letras': contador_letras
            }
        else:
            contador[palabra]['cantidad'] += 1
    return contador

if (__name__ == "__main__"):
    lista_palabras = ["hola", "como", "estas"]

    print(contar_letras(lista_palabras))