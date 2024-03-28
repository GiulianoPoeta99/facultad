"""
8. Manipulación de Cadenas: Solicite al usuario que ingrese una frase. El programa debe 
contar cuántas veces aparece cada vocal en la frase e imprimir los resultados.
"""

frase = input("Ingrese una frase: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    cantidad = frase.lower().count(vocal)
    print(f"La vocal {vocal} aparece {cantidad} veces.")