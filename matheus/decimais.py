print("="*40)
print("CLACULANDO MÉDIA")
print("="*40)
quantidade = int(input("quantidade de alunos: "))

media = 0

for i in range(quantidade):
    nome = input(f"Nome aluno {i+1} :  ")
    nota = float(input(f"Nota do aluno  {i+1} {nome}: "))

    media += nota/quantidade

print("="*40)
print("RESULTADO")

print("="*40)
print(f"Média das nota1 {nome} e nota2: {nota} : {media:.2f}")