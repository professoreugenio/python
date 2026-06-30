class Banco:
    def __init__(self,cliente="Paula Lins",saldo=12450.89,senha=123456,status=False):
        self.cliente = cliente
        self.saldo = saldo
        self.senha = senha
        self.status = status
        
    def login(self,senhadigitada):
        if(senhadigitada!=self.senha):
            print(f"Senha não confere")
        else:
            self.status = True
            print(f"""
            =================================
            😀 Acesso liberado""")
    def exibirsaldo(self):
        if self.status == True:
            print(f"""
DADOS BANCÁRIOS
NOME DO CLIENTE: {self.cliente}
SALDO ATUAL: R$ {self.saldo:.2f}
                """)
        else:
            print("Saldo : *************")
        
cliente = Banco()

while cliente.status == False:
    senha_inserida = input("😎 DIGITE A SENHA: ")
    if(senha_inserida == ""):
        print("🙄 Senha não pode ser vazia")
    elif (senha_inserida.isdigit()==False):
        print("😒 Digite apenas números")
    elif (len(senha_inserida)!=6):
        print("😫 DIGITE SUA SENHA DE 6 DÍGITOS")
    else:
        senha_inserida = int(senha_inserida)
        cliente.login(senha_inserida)
        
cliente.exibirsaldo()
            