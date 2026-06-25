class Banco:
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
            return f"""
            DADOS D CLIENTE
            Nome {self.cliente}
            Saldo {self.saldo}
            """


cliente = Banco()
print(cliente.logar(123))
print(cliente.exibirsaldo())