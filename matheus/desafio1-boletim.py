print("=" * 40)
print("Boletim da Turma")
print("=" * 40)

quantidade = int(input("Quantos alunos?"))

somanotas = 0

for i in range(quantidade):
    nome = input(f"Nome do aluno {i+1}:")
    nota = float(input(f"Nota de {nome}:"))
    somanotas += nota
    if(nota>=7):
        print("Aprovado")
    else:
        print("Reprovado")

print("="*40)
if quantidade > 0:
    media = somanotas / quantidade
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhum aluno cadastrado.")
