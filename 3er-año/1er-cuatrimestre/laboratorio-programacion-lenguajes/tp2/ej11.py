"""
11.  Introducción a las Clases: Desarrolle una clase llamada Auto, que contenga atributos 
como marca, modelo y kilometraje. Incluya un método mostrar_descripcion() que 
imprima la información del auto y otro método viajar() que acepte una cantidad de 
kilómetros y los añada al kilometraje del auto. 
"""

class Auto:
    def __init__(self, marca, modelo, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje

    def mostrar_descripcion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Kilometraje: {self.kilometraje}")

    def viajar(self, distancia):
        self.kilometraje += distancia