from atividades_herança.heranca_veiculo.classVeiculos import Veiculo

class Carro(Veiculo):
    def __init__(self,modelo,marca,ano,portas):
        super().__init__(modelo,marca,ano)
        self.portas = portas
    def mostarPortas(self):
        print(f"""
        Quantidade de Portas {self.portas}""")   
        