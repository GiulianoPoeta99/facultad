"""
9. Listas por comprensión: Dada una lista de números, utilice una comprensión de lista para 
generar una nueva lista que contenga únicamente los números pares de la lista original.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]
print(pares)