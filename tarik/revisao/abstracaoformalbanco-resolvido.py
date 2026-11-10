from abc import ABC, abstractmethod


class BancoAbstrato(ABC):
    def __init__(self, titular="Maria do Carmo", saldo=5650.49, senha=123456):
        self._titular = titular
        self._saldo = saldo
        self._senha = senha
        self._logado = False

    @property
    def logado(self):
        return self._logado

    @abstractmethod
    def validar_senha_digitada(self, senha_digitada):
        pass

    @abstractmethod
    def logar(self, inputsenha):
        pass

    @abstractmethod
    def exibirsaldo(self):
        pass


class Banco(BancoAbstrato):
    def validar_senha_digitada(self, senha_digitada):
        if senha_digitada == "":
            print("O campo senha está vazio")
            return None

        elif senha_digitada.isdigit() == False:
            print("Digite apenas números")
            return None

        else:
            return int(senha_digitada)

    def logar(self, inputsenha):
        if inputsenha != self._senha:
            self._logado = False
            print("Senha não confere.")
        else:
            self._logado = True
            print("Acesso liberado.")

    def exibirsaldo(self):
        if self._logado != True:
            print("Saldo: ***********")
        else:
            print(f"""                  
DADOS BANCÁRIOS
CLIENTE: {self._titular}
SALDO: R$ {self._saldo:.2f}
""")


cliente = Banco()

while cliente.logado == False:
    senha_digitada = input("Digite a senha: ")

    senha_validada = cliente.validar_senha_digitada(senha_digitada)

    if senha_validada is not None:
        cliente.logar(senha_validada)

cliente.exibirsaldo()