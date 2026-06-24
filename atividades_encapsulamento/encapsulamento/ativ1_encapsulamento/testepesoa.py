class Pessoa:
    def __init__(self,nome):
        self.__nome = nome;
    def nomepessoa(self):
        print(f"Nome registrado {self.__nome}");


pessoa1 = Pessoa("Paula Lins")
# print(pessoa1.__nome);
pessoa1.nomepessoa()