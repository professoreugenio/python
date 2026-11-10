qdeposito = int(input("quantidade de depósito: "))

saldoinicial = float(500.89)
ttldeposito = 0
saldofinal = saldoinicial
ttlsaque =0
alerta = 0

for i in range(qdeposito):
    deposito = float(input(f"Valor depósito {i+1}: "))
    ttldeposito +=deposito
    saldofinal = ttldeposito + saldoinicial
print("="*40)
print(f"saldo INICIAL:R$ {saldoinicial:.2f}")
print(f"Total depósitos:R$ {ttldeposito}",f"{i+1}")
print(f"saldo atual:R$ {saldofinal:.2f}")
print(" ")

qsaque = int(input("quantidade de saques: "))

for i in range(qsaque):
    saque = float(input(f"Valor do {i+1}º saque: "))
    if(saque<0):
        print(f"Valor inválido")
        alerta = 1
    if(saque>saldofinal):
        print(f"Saldo insuficiente {saldofinal:.2f}")
        alerta = 1
    ttlsaque += saque
    saldofinal -= saque

if alerta == 1:
    print("="*40)
    print("Saque não realizado")
    print("="*40)
else:
    print(" ")
    print("="*40)
    print("TOTAL DEPÓSITO",f"R$ {ttldeposito:.2f}")
    print("TOTAL SAQUE",f"R$ {ttlsaque:.2f}")
    print("SALDO inicial",f"R$ {saldoinicial:.2f}")
    print("SALDO FINAL",f"R$ {saldofinal:.2f}")


