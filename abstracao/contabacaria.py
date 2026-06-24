from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def adicionar_saldo(self, valor):
        self.__saldo += valor

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def mostrar_saldo(self):
        pass


class ContaBancaria(Conta):
    def depositar(self, valor):
        if valor > 0:
            self.adicionar_saldo(valor)
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")


conta = ContaBancaria("Paula", 1000)
conta.depositar(200)
conta.mostrar_saldo()