
print("=" * 40)
print("Caixa Eletrônico")
print("=" * 40)

saldo = 500

print(f"Saldo inicial: R$ {saldo:.2f}")

quantidade = int(input("Quantas operações? "))

for i in range(quantidade):
    print(f"\nOperação {i + 1}")

    operacao = input(
        "[D]epósito ou [S]aque: "
    ).strip().upper()

    if operacao != "D" and operacao != "S":
        print("Operação inválida!")
        print(f"Saldo atual: R$ {saldo:.2f}")
        continue

    valor = float(input("Valor: "))

    if valor <= 0:
        print("O valor deve ser maior que zero!")

    elif operacao == "D":
        saldo += valor
        print("Depósito realizado!")

    elif operacao == "S":
        if valor <= saldo:
            saldo -= valor
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")

    print(f"Saldo atual: R$ {saldo:.2f}")

print("-" * 40)
print(f"Saldo final: R$ {saldo:.2f}")
