class Veiculo:
    def __init__(self,modelo,marca,ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
    def apresentar(self):
        print(f"""
        DADOS DO VEÍCULO
        
        MODELO : {self.modelo}    
        MARCA : {self.marca}    
        ANO : {self.ano}
              """)