"""
15.  Manejo de Excepciones: Desarrolle una función dividir que tome dos números y devuelva 
el resultado de su división. Implemente un manejo de excepciones para capturar la 
división por cero, mostrando un mensaje apropiado en tal caso.
"""

def dividir(num1, num2):
    try:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("No se puede dividir por cero.")

# Ejemplo de uso:
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
dividir(num1, num2)