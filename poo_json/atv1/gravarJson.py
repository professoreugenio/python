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


produto1 = Produto("Notebook",3750.89, 45)

dados_produto = produto1.to_dict()

with open("produto.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_produto, arquivo, indent=4, ensure_ascii=False)

print("Produto salvo com sucesso!")