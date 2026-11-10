
print("=" * 40)
print("Estacionamento")
print("=" * 40)

quantidade = int(input("Quantos carros hoje? "))

total = 0

for i in range(quantidade):
    horas = int(input(f"Horas do carro {i + 1}: "))

    if horas <= 0:
        valor = 0
    elif horas == 1:
        valor = 5
    else:
        valor = 5 + (horas - 1) * 3

    print(f"Carro {i + 1} paga: R$ {valor:.2f}")

    total += valor

print("-" * 40)
print(f"Total arrecadado: R$ {total:.2f}")
