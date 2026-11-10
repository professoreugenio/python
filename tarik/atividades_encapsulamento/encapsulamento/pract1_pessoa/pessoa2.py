class Pessoa:
    def __init__(self,nome):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nomenovo):
        nomenovo = nomenovo.strip()
        if(nomenovo==""):
            print(f"Campo vazio, defina um nome")
        else:
            self.__nome = nomenovo
    def exibir(self):
        print(f"Nome cadastrado: {self.__nome}")
        
pessoa1 = Pessoa("JOÃO PAULO")
pessoa1.nome = "ANDRÉ"

pessoa1.exibir()