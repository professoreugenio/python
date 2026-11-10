
print("=" * 40)
print("Aumento de Salário")
print("=" * 40)

quantidade = int(input("Quantos funcionários? "))

total_folha = 0

for i in range(quantidade):
    nome = input("Nome: ")
    salario = float(input("Salário: "))

    if salario < 2000:
        percentual = 15
    else:
        percentual = 10

    aumento = salario * percentual / 100
    novo_salario = salario + aumento

    total_folha += novo_salario

    print(
        f"{nome} recebeu {percentual}% de aumento"
        f" -> R$ {novo_salario:.2f}"
    )

print("-" * 40)
print(f"Total da folha: R$ {total_folha:.2f}")
