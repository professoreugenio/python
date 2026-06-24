class ContaBancaria:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def pagar(self, valor, senha_digitada):
        if senha_digitada != self.__senha:
            print("Senha inválida.")
            return

        if valor <= 0:
            print("Valor inválido.")
            return

        if valor > self.__saldo:
            print("Saldo insuficiente.")
            return

        self.__saldo -= valor
        print("Pagamento autorizado.")
        print("Saldo atualizado.")
        print("Comprovante gerado.")
        
conta = ContaBancaria("Paula", 1000, "1234")
conta.pagar(200, "1234")