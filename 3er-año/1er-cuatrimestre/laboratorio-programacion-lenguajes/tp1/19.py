class Persona2:
    def __init__(self, nombre, edad, genero):
        """
        Constructor de la clase Persona.

        Parámetros:
            nombre (str): El nombre de la persona.
            edad (int): La edad de la persona.
        """

        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def __str__(self):
        """
        Método para obtener una representación en cadena de la persona.

        Retorna:
            str: Una cadena que representa la persona.
        """
        
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Genero: {self.genero}"