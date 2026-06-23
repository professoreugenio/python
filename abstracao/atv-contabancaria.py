class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito realizado com sucesso.")

    def mostrar_saldo(self):
        print(f"Saldo: R$ {self.__saldo:.2f}")


conta = ContaBancaria("Paula", 1000)
conta.depositar(200)
conta.mostrar_saldo()
