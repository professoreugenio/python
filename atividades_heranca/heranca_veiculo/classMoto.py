from atividades_herança.heranca_veiculo.classVeiculos import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo,marca,ano):
        super().__init__(self,modelo,marca,ano)
        self.cilindrada = cilindrada
    def mostrar_cilindrada():
        print(f"Cilindradas: {self.cilindradas}")