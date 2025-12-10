class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito realizado: {cantidad}€")
        self.mostrar_saldo()

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No se dispone de saldo suficiente.")
        elif cantidad <= 0:
            print("Cantidad de retiro no válida.")
        else:
            self.saldo -= cantidad
            print(f"Retiro realizado: {cantidad}€")
        self.mostrar_saldo()

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.saldo}€\n")



cuenta = CuentaBancaria("Javier Gutiérrez")

cuenta.depositar(500)
cuenta.depositar(499)
cuenta.retirar(1100)
