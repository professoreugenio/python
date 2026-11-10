
print("=" * 40)
print("Pares e Ímpares")
print("=" * 40)

quantidade = int(input("Quantos números? "))

pares = 0
impares = 0
soma_pares = 0

for i in range(quantidade):
    numero = int(input(f"Número {i + 1}: "))

    if numero % 2 == 0:
        pares += 1
        soma_pares += numero
    else:
        impares += 1

print("-" * 40)
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Soma dos pares: {soma_pares}")
