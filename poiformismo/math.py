import math

class Calculos:
    def __init__(self):
        print(f"MEDIDA DO PI")
        mpi = math.pi
        print(f"{mpi:.4f}")
        print(f"CONSTANTE DE EULER")
        mpi = math.e
        print(f"{mpi:.2f}")
    def raiz(self,valor):
        self.valor = valor
        print(f"Raiz quadrada de {valor}")
        raiz = math.sqrt(self.valor)
        print(f"Resultado {raiz:.2f}")
        
    def potencia(self,base,expoente):
        self.base = base
        self.expoente = expoente
        print(f"A potência de {self.base} elevado a {self.expoente} é igual: ")
        calcpotencia = math.pow(base,expoente)
        print(f"Resultado: {calcpotencia}")

Calculos()
raizquadrada = Calculos()
potencia = Calculos()
raizquadrada.raiz(100)
potencia.potencia(9,2)
        
