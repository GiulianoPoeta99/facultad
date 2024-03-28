"""
13.  Polimorfismo: Implemente una clase base Animal con un método hacer_sonido() que 
imprima "Este animal hace un sonido". Luego, desarrolle clases derivadas Perro y Gato, 
sobrescribiendo el método hacer_sonido() para que imprima "Guau" y "Miau", 
respectivamente. 
"""

class Animal:
    def hacer_sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")