class Lojas:
    def __init__(self):
        print(f"LOJA PGAMENTOS")
        print(f"=====================\n")
        
class PagamentoPix():
    def pagar(self,valor):
        print(f"Pagamento via pix no valor de {valor:.2f}.")

class PagamentoCartao():
    def pagar(self,valor):
        self.valor = valor
        perc = 0.055
        taxacartao = self.valor * perc
        conv = perc * 100
        valorfinal = valor + taxacartao
        print(f"""
        Pagamento via cartão no valor de R$ {valor:.2f}
        Será cobrada uma taxa de {conv:.2f}%
        Valor final do pagamento R$ {valorfinal:.2f}.""")

class PagamentoBoleto():
    def pagar(self,valor):
        print(f"==========================================")
        print(f"""Pagamento realizado em boleto
    Valor de {valor:.2f}""")
        
Lojas()        
pagamentos = [PagamentoPix(),PagamentoCartao(),PagamentoBoleto()] 

for pagamento in pagamentos:
    pagamento.pagar(200)       