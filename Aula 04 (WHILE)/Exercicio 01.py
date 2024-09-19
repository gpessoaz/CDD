n = 0
nota = 0
soma = 0
while n < 10:
    n = n + 1
    nota = float(input("Digite a nota: "))
    soma = soma + nota
media = soma / n
print(f"A média geral é {media}")
