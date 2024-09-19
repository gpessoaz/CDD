opcao = 1
while opcao != 2:
    n1 = int(input("Digite o primeiro numero: "))
    if n1 == 0:
        while n1 == 0:
            n1 = int(input("Valor inválido, digite outro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    if n2 == 0:
        while n2 == 0:
            n2 = int(input("Valor inválido, digite outro numero: "))
    div = n1 / n2
    print(div)
    opcao = int(input("Deseja continuar \n""1 para sim\n""2 para não: "))