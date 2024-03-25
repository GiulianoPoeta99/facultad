def es_primo(num: int) -> bool:
    """
    Función que verifica si un número dado es primo.

    Parámetros:
        num (int): El número que se verificará si es primo.

    Retorna:
        bool: True si el número es primo, False en caso contrario.
    """
     
    if (num <= 1):
        return False
    elif (num <= 3):
        return True
    elif ((num % 2) == 0) | ((num % 3) == 0):
        return False
    i = 5
    while ((i * i) <= num):
        if (((num % i) == 0) | (num % (i + 2) == 0)):
            return False
        i += 6
    return True

def encontrar_primos(n: int) -> list[int]:
    """
    Función que encuentra todos los números primos hasta el número dado.

    Parámetros:
        n (int): El número entero positivo hasta el cual se buscarán los primos.

    Retorna:
        list: Una lista de números primos hasta n.
    """
    
    primos = []
    for i in range(1, n + 1):
        if (es_primo(i)):
            primos.append(i)
    return primos

if (__name__ == "__main__"):
    n = int(input("Ingrese un número entero positivo para encontrar los números primos hasta ese número: "))
    print(f"Los números primos hasta {n} son: ", encontrar_primos(n))