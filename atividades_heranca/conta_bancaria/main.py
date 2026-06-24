class ContaBancaria:
    def __init__(self, titular, saldo): #método (def) método construtor
        # titular, saldo são parâmetros
        self.titular = titular # parâmetros : self.titular
        self.__saldo = saldo

    def depositar(self, valor): #método de classe depositar
        if valor > 0:
            self.__saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")


conta1 = ContaBancaria("Ana", 1000)

conta1.depositar(300)
conta1.sacar(-7000)
conta1.mostrar_saldo()