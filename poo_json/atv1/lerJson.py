import json

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def to_dict(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "estoque": self.estoque
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["nome"],
            dados["preco"],
            dados["estoque"]
        )

    def mostrar_dados(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Estoque: {self.estoque}")


with open("produto.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

produto1 = Produto.from_dict(dados)

produto1.mostrar_dados()