class Pessoa:
    def __init__(self, nome):  # Método construtor
        self.nome = nome     # Atributo privado

   
pessoa = Pessoa("PAULA LINS")  # Objeto / instância da classe Pessoa
print(pessoa.nome)        # Chamada do getter / leitura da propriedade nome