"""
12.  Herencia: Extienda la clase Auto para crear una nueva clase Camioneta, que herede de 
Auto pero añada un atributo adicional llamado capacidad_carga (en kilogramos). Incluya 
un método verificar_carga() que determine si un peso dado puede ser transportado.
"""

from .ej11 import Auto

class Camioneta(Auto):
    def __init__(self, marca, modelo, kilometraje, capacidad_carga):
        super().__init__(marca, modelo, kilometraje)
        self.capacidad_carga = capacidad_carga

    def verificar_carga(self, peso):
        if peso <= self.capacidad_carga:
            print("La carga puede ser transportada.")
        else:
            print("La carga excede la capacidad de la camioneta.")