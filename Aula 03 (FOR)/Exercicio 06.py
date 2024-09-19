soma = 0
for i in range(1,11):
    num = int(input("Digite um numero: "))
    if num%2 != 0:
        soma = soma + num
print(soma)