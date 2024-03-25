class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        """
        Inicializa un objeto Libro con el título, autor y año de publicación dados.

        Parámetros:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            anio_publicacion (int): El año de publicación del libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def __str__(self):
        """
        Retorna una representación de cadena del objeto Libro.
        """
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.anio_publicacion}"
