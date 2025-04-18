class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def hacer_sonido(self):
        print(f"El {self.nombre} hace un sonido")
    
class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace Guau Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace Miau")

class Vaca(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace Muuu")

animal1=Perro("Andy")
animal2=Gato("Mirringo")
animal3=Vaca("Lola")

zoologico=[animal1,animal2,animal3]

for animal in zoologico:
    animal.hacer_sonido()