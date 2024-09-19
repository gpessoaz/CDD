x = 1
soma = 0
alunos = int(input("Quantos alunos existem nesta turma: "))
while x <= alunos:
    nota = float(input(f"Digite a nota deste {x} aluno: "))
    x = x + 1
    soma = soma + nota
media = soma / alunos
print(f"A média geral é {media}")
