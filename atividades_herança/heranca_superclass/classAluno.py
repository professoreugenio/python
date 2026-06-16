from atividades_herança.heranca_superclass.classPessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self,nome,idade,nota):
       super().__init__(nome,idade)
       self.nota = nota
    def estudar(self):
        print(f"{self.nome} está estudando e nota: {self.nota}")
