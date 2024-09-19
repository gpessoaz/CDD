escolha = 0
while escolha == 0:
    num = int(input("Digite um numero: "))

    if num > 0:
        if num%2 == 1:
            print("O numero é positivo e impar ")
        else:
            print("O numero é posivito e par")

    else:
        if num%2 == 1:
            print("O numero é negativo e impar ")
        else:
            print("O numero é negativo e par")
    escolha = int(input("Desejar continuar? \n 0 = continuar \n 1 = sair"))



