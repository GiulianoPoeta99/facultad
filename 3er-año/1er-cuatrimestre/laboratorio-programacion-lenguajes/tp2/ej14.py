"""
14.  Composición: Construya una clase Libreria que contenga una lista de instancias de otra 
clase, Libro, la cual debe tener atributos como titulo, autor y año_publicacion. La clase 
Libreria debe incluir métodos para agregar y remover libros, además de un método para 
mostrar todos los libros disponibles. 
"""

class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

class Libreria:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def remover_libro(self, libro):
        self.libros.remove(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Año de Publicación: {libro.año_publicacion}")