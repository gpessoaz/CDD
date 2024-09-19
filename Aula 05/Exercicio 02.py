opcao = 0
while opcao == 0:
    n1 = float(input("Digite a primeira nota: "))
    while n1 < 0 or n1 > 10:
        n1 = float(input("Nota fora da faixa,\n"
                     "Digite a primeira nota: "))

    n2 = float(input("Digite a segunda nota: "))
    while n2 < 0 or n2 > 10:
        n2 = float(input("Nota fora da faixa,\n"
                     "Digite a segunda nota: "))
    media = (n1+n2)/2
    print(media)
    opcao = int(input("Deseja continuar?: 0- continuar"
                      " 1- finalizar "))