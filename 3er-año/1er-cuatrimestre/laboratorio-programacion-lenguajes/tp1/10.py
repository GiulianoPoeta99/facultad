from . import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, num_estudiante, notas):
        """
        Constructor de la clase Estudiante.

        Parámetros:
            nombre (str): El nombre del estudiante.
            edad (int): La edad del estudiante.
            num_estudiante (int): El número de estudiante del estudiante.
            notas (list): Una lista de notas del estudiante.
        """

        super().__init__(nombre, edad)
        self.num_estudiante = num_estudiante
        self.notas = notas

    def calcular_promedio(self):
        """
        Método para calcular el promedio de las notas del estudiante.

        Retorna:
            float: El promedio de las notas del estudiante.
        """
        
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)