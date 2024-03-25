class Libro2:
    def __init__(self, titulo, autor, anio_publicacion, genero):
        """
        Inicializa un objeto Libro con el título, autor y año de publicación dados.

        Parámetros:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            anio_publicacion (int): El año de publicación del libro.
            genero (str): Genero literario del libro
        """
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.genero = genero

    def __str__(self):
        """
        Retorna una representación de cadena del objeto Libro.
        """
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.anio_publicacion}"
    
    @staticmethod
    def buscar_por_genero(lista_libros, genero):
        """
        Busca libros por género en una lista de libros.

        Parámetros:
            lista_libros (list): Una lista de objetos Libro.
            genero (str): El género literario a buscar.

        Retorna:
            list: Una lista de libros que pertenecen al género especificado.
        """
        libros_encontrados = []
        for libro in lista_libros:
            if (libro.genero.lower() == genero.lower()):
                libros_encontrados.append(libro)
        return libros_encontrados
