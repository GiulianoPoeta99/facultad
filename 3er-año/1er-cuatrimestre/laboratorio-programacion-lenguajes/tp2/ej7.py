"""
7. Diccionarios: Cree un diccionario que contenga información sobre un libro, incluyendo: 
título, autor, año de publicación y género. Desarrolle un programa que imprima cada 
detalle en líneas separadas.
"""

libro = {
    "titulo": "El Quijote",
    "autor": "Miguel de Cervantes",
    "año de publicación": 1605,
    "género": "Novela"
}

for clave, valor in libro.items():
    print(f"{clave}: {valor}")