class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.materias=[]

    def agregar_materia(self,materia):
        self.materias.append(materia)

    def mostrar_materias(self):
        if not self.materias:
            print(f"{self.nombre} no esta inscrito en ninguna materia")
        else:
            print(f"{self.nombre} esta inscrito en las siguientes materias")
            for materia in self.materias:
                print(f"- {materia}")

estudiante1=Estudiante("Isabela",23)
estudiante1.agregar_materia("Matematicas")
estudiante1.agregar_materia("Español")
estudiante1.mostrar_materias()
