class Banco():
    def __init__(self,titular="Maria do Carmo",saldo=5500,senha=12345):
        self.saldo = saldo
        self.titular = titular
        self.senha = senha
        self.logado = False
    
    def logar(self, inputsenha):
        if(inputsenha !=self.senha):
            self.logado = False
            print(f"Senha não confere. Tente novamente")
        else :
            self.logado = True
            print(f"Logado com sucesso")
            
    def exibirsaldo(self):
        if(self.logado == False):
            print(f"SALDO: *********")
        else:
            print (f"""
    DADOS BANCÁRIOS
    NOME CLIENTE: {self.titular}
    SALDO ATUAL: {self.saldo}            
               """)
    def status(self):
        status = self.logado
        print(status)
       
cliente = Banco()

while cliente.logado == False:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == "":
       
        print("Erro: Senha vazia")
    elif senha_digitada.isdigit() == False:
       
        print("Digite apenas números")
        
    else:
        senha_digitada = int(senha_digitada)
        cliente.logar(senha_digitada)
        
            
    
cliente.exibirsaldo()
