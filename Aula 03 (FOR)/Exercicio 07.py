alunos = int(input("Quantos alunos existem nesta turma:" ))
soma = 0
for x in range(alunos):
    nota = float (input(f"Digite a nota deste {x+1} aluno: "))
    soma = soma + nota
média = soma / alunos
print (média)


