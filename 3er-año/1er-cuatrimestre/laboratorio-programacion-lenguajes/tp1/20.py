from . import Persona2

class Estudiante2(Persona2):
    def __init__(self, nombre, edad, genero, num_estudiante):
        """
        Constructor de la clase Estudiante.

        Parámetros:
            nombre (str): El nombre del estudiante.
            edad (int): La edad del estudiante.
            genero (str): El genero de la persona.
            num_estudiante (int): El número de estudiante del estudiante.
        """

        super().__init__(nombre, edad, genero)
        self.num_estudiante = num_estudiante
        self.notas = []

    def agregar_nota(self, nota):
        """
        Método para agregar una nota a la lista de notas del estudiante.

        Parámetros:
            nota (float): La nota a agregar.
        """
        self.notas.append(nota)

    def calcular_promedio(self):
        """
        Método para calcular el promedio de las notas del estudiante.

        Retorna:
            float: El promedio de las notas del estudiante.
        """
        if (len(self.notas) == 0):
            return 0
        return sum(self.notas) / len(self.notas)

    def escala_calificaciones(self):
        """
        Método para mostrar el promedio en una escala de calificaciones.

        Retorna:
            str: La calificación correspondiente al promedio del estudiante.
        """
        promedio = self.calcular_promedio()
        if (promedio >= 9):
            return "Excelente"
        elif (promedio >= 7):
            return "Muy Bueno"
        elif (promedio >= 5):
            return "Bueno"
        elif (promedio >= 4):
            return "Regular"
        else:
            return "Insuficiente"
