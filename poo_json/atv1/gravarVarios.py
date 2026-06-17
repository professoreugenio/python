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
        print(f"{self.nome} - R$ {self.preco:.2f} - Estoque: {self.estoque}")


produtos = [
    Produto("Computador", 2300.00, 10),
    Produto("Monitor", 700.00, 10),
    Produto("Placa de Vídeo", 1200.00, 30)
]

lista_produtos = []

for produto in produtos:
    lista_produtos.append(produto.to_dict())

with open("produtos.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista_produtos, arquivo, indent=4, ensure_ascii=False)

print("Lista de produtos salva com sucesso!")