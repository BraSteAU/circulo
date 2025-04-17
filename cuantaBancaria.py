class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo=saldo
    
    def depositar(self,cantidad):
        self.saldo+=cantidad
        print(f"Se han depositado {cantidad}")

    def retirar(self,cantidad):
        if self.saldo<cantidad:
            print("Saldos insuficientes")
        else:
            self.saldo-=cantidad
            print(f"Se han retirado {cantidad}")
    
    def mostrar_saldo(self):
        print(f"El saldo actual es: {self.saldo}")

cuentabancaria=CuentaBancaria("Isabela",2000000)
cuentabancaria.depositar(500000)
cuentabancaria.mostrar_saldo()
cuentabancaria.retirar(3000000)
cuentabancaria.mostrar_saldo()

    