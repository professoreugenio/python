class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")


conta1 = ContaBancaria("Ana", 100)

conta1.depositar(50)
conta1.sacar(1000)
conta1.mostrar_saldo()