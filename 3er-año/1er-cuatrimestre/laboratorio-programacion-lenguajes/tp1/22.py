class Biblioteca2:
    def __init__(self):
        """
        Constructor de la clase Biblioteca.
        Inicializa una lista vacía de libros y un diccionario vacío de préstamos.
        """

        self.libros = []
        self.prestamos = {}

    def prestar_libro(self, libro, persona):
        """
        Método para prestar un libro a una persona.

        Parámetros:
            libro (Libro): El objeto Libro a prestar.
            persona (str): El nombre de la persona a la que se prestará el libro.
        """

        if (libro in self.libros):
            if (libro not in self.prestamos):
                self.prestamos[libro] = persona
                print(f"El libro '{libro.titulo}' ha sido prestado a '{persona}'.")
            else:
                print(f"El libro '{libro.titulo}' ya está prestado.")
        else:
            print("El libro no está disponible en la biblioteca.")

    def devolver_libro(self, libro):
        """
        Método para devolver un libro prestado.

        Parámetros:
            libro (Libro): El objeto Libro a devolver.
        """

        if (libro in self.libros):
            if (libro in self.prestamos):
                del self.prestamos[libro]
                print(f"El libro '{libro.titulo}' ha sido devuelto.")
            else:
                print(f"El libro '{libro.titulo}' no está actualmente prestado.")
        else:
            print("El libro no está disponible en la biblioteca.")

    def libros_prestados(self):
        """
        Método para imprimir los libros prestados.
        """

        if (self.prestamos):
            print("Libros prestados:")
            for libro, persona in self.prestamos.items():
                print(f"- '{libro.titulo}' prestado a '{persona}'")
        else:
            print("No hay libros actualmente prestados.")

    def libros_disponibles(self):
        """
        Método para imprimir los libros disponibles (no prestados).
        """
        
        libros_disponibles = [libro for libro in self.libros if libro not in self.prestamos]
        if (libros_disponibles):
            print("Libros disponibles:")
            for libro in libros_disponibles:
                print(f"- '{libro.titulo}'")
        else:
            print("No hay libros disponibles en la biblioteca.")
