from classPessoa import Pessoa

class Professor(Pessoa):
    def __init__(self,nome,idade,salario):
        super().__init__(nome,idade)
        self.salario = salario
    def ensinar(self):
        print(f"O professor ensina e recebe {self.salario} ")
        
        
        