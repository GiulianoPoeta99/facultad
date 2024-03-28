"""
2. Estructuras de Control - Condicionales: Desarrolle un programa que requiera del usuario 
la introducción de un número. Si el número es positivo, debe mostrar el mensaje "El 
número es positivo". Si es negativo, "El número es negativo". Y si es cero, "El número es 
cero".
"""

numero = float(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")