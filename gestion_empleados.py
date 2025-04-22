class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    
class Empresa():
    def __init__(self, ):
        self.empleados={}

    def agregar_empleado(self,nombre,cargo,salario):
        self.empleados[nombre]={"nombre":nombre,"cargo":cargo,"salario":salario}

    def mostrar_empleados(self):
        if not self.empleados:
            print("no hay empleados registrados")
        else:
            for nombre,info in self.empleados.items():
                print(f"Nombre: {nombre} / Cargo: {info['cargo']} / Salario: {info['salario']}")

    def calcular_promedio(self):
        salarios=0
        for info in self.empleados.values():
            salarios+=info["salario"]
        promedio=salarios/len(self.empleados) if self.empleados else 0
        print(f"Promedio de salarios: {promedio:.2f}")

    def buscar_empleado(self,nombre):
        if nombre in self.empleados:
            info=self.empleados[nombre]
            print(f"Nombre: {nombre} / Cargo: {info['cargo']} / Salario: {info['salario']}")
        else:
            print("El empleado no existe")
    

empresa=Empresa()
empresa.agregar_empleado("Isabela", "Community Manager", 2200000)
empresa.agregar_empleado("Brayan", "Auxiliar", 1600000)
empresa.mostrar_empleados()
empresa.calcular_promedio()
empresa.buscar_empleado("Isabela")

    
    
