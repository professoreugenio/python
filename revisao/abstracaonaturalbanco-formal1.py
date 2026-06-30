from abc import ABC, abstractmethod

class BancoAbstracao(ABC):

    @abstractmethod
    def logar(self,senhainput):
        pass

    @abstractmethod
    def exibirsaldo(self):
        pass



class Banco(BancoAbstracao):
    def __init__(self,cliente="Maria do Carmo",saldo=2500, senha=1234):
        self.cliente = cliente
        self.saldo = saldo
        self.senha = senha
        self.logado = False

    def logar(self,senhainput):
        if (senhainput != self.senha):
            self.logado = False
            return f"Senha não confere. Tente novamente"
        else:
            self.logado = True
            return f"Conectado com sucesso"
    def exibirsaldo(self):
        if(self.logado == False):
            return f"Acesso negado para saldo"
        else:
            self.logado == True
            return f"""
            DADOS D CLIENTE
            Nome {self.cliente}
            Saldo {self.saldo}
            """

cliente = Banco()

while cliente.logado == False:
    senha_digitada = input('DIGITE A SENHA:')
    if senha_digitada=="":
        print("Campo não pode estar vazio")
    elif senha_digitada.isdigit()==False:
        print("Campo não pode letras")
    elif len(senha_digitada) !=4:
        print("Senha com 4 dígitos")
    else:
        senha_digitada = int(senha_digitada)
        print(cliente.logar(senha_digitada))

print(cliente.exibirsaldo())