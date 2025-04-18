class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.materias={}

    def agregar_materia(self,materia,nota):
        self.materias[materia]=nota

    def calcular_promedio(self):
        notas=0
        for nota in self.materias.values():
            notas+=nota
        promedio=notas/len(self.materias) if self.materias else 0
        print(f"Promedio de notas: {promedio:.2f}")

    def mostrar_materias(self):
        if not self.materias:
            print(f"{self.nombre} no esta inscrito en ninguna materia")
        else:
            print(f"{self.nombre} esta inscrito en las siguientes materias")
            for materia,nota in self.materias.items():
                print(f"- {materia} : {nota}")

estudiante1=Estudiante("Isabela",23)
estudiante1.agregar_materia("Matematicas",4.5)
estudiante1.agregar_materia("Español",3.8)
estudiante1.mostrar_materias()
estudiante1.calcular_promedio()
