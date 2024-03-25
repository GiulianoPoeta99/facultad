class Biblioteca:
    def __init__(self):
        """
        Constructor de la clase Biblioteca.
        Inicializa una lista vacía de libros.
        """

        self.libros = []

    def agregar_libro(self, libro):
        """
        Método para agregar un libro a la biblioteca.

        Parámetros:
            libro (Libro): El objeto Libro a agregar a la biblioteca.
        """
         
        self.libros.append(libro)

    def imprimir_libros(self):
        """
        Método para imprimir la lista de libros en la biblioteca.
        Imprime un mensaje si la biblioteca está vacía.
        """
        
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Lista de libros en la biblioteca:")
            for libro in self.libros:
                print(libro)

