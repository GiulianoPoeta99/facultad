"""
4. Estructuras de Control - Bucles con While: Diseñe un programa que solicite la 
introducción de números de manera iterativa. Este programa deberá sumar los números 
ingresados y finalizar cuando la suma exceda 100, mostrando el total acumulado. 
"""

suma = 0
while suma <= 100:
    numero = float(input("Ingrese un número: "))
    suma += numero
print("Total acumulado:", suma)