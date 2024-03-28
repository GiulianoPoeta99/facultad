"""
6. Listas y Bucles: Elabore un programa que solicite la entrada de 5 nombres, almacénelos en 
una lista y luego los imprima en orden inverso.  
"""

nombres = []
for i in range(5):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
for nombre in reversed(nombres):
    print(nombre)