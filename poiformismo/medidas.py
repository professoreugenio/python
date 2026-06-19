import math


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado


class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio * self.raio


formas = [
    Retangulo(5, 3),
    Quadrado(4),
    Circulo(2)
]

for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")
