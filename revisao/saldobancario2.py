class Banco:
    def __init__(self, titular="Maria do Carmo", saldo=5650.49, senha=123456):
        self.titular = titular
        self.saldo = saldo
        self.senha = senha
        self.logado = False

    def logar(self, inputsenha):
        if (inputsenha != self.senha):
            self.logado = False
            print("Senha não confere.")
        else:
            self.logado = True
            print("Acesso liberado.")

    def exibirsaldo(self):
        if (self.logado != True):
            print(f"Saldo : ***********")
        else:
            print(f"""                  
            DADOS BANCÁRIOS
            CLIENTE: {self.titular}
            SALDO : {self.saldo}
            """)


cliente = Banco()

while cliente.logado == False:
    senha_digitada = input("Digite a senha")
    if senha_digitada == "":
        print("O campo senha está vazio")
    elif senha_digitada.isdigit()==False:
        print("Digite apenas números")
    else:
        senha_digitada = int(senha_digitada)
        cliente.logar(senha_digitada)

cliente.exibirsaldo()