import json

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["nome"],
            dados["preco"],
            dados["estoque"]
        )

    def mostrar_dados(self):
        print(f"{self.nome} - R$ {self.preco:.2f} - Estoque: {self.estoque}")


with open("produtos.json", "r", encoding="utf-8") as arquivo:
    dados_json = json.load(arquivo)

produtos = []

for item in dados_json:
    produto = Produto.from_dict(item)
    produtos.append(produto)

for produto in produtos:
    produto.mostrar_dados()