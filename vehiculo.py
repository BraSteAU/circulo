class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
class Carro(Vehiculo):
    def conducir(self):
        print(f"El carro {self.marca} del {self.modelo} esta arrancando")
    
class Moto(Vehiculo):
    def conducir(self):
        print(f"La moto {self.marca} del {self.modelo} esta frenando")

moto=Moto("TVS APACHE",2023)
carro=Carro("Chevrolet Camaro",1968)
carro.conducir()
moto.conducir()
        