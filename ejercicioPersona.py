class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def presentarse(self):
        print(f"Hola, me llamo ",self.nombre," y tengo ",self.edad," años")
    
persona1=Persona("Brayan",27)
persona1.presentarse()
        