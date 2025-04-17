import math

class Circulo:
    def __init__(self,radio):
        self.radio=radio
    
    def calcular_area(self):
        area=math.pi*(self.radio**2)
        print(f"El area del circulo con radio {self.radio} es: {area}")
    
circulo=Circulo(7)
circulo.calcular_area()
        