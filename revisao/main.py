class Aluno():
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def dadosaluno(self):
        return f"""Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}"""
        pass


# TERMINAL: ABSTRAÇÃO NATURAL
aluno1 = Aluno("Paula", 46, "Programador de Sistema")
print(aluno1.dadosaluno())
