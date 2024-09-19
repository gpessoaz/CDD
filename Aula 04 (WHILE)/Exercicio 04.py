opc = 1
while opc != 2:
    x = 1
    num = int(input("Digite um número: "))
    while x <= 10:
        mult = num * x
        print(f"{x}x{num}={mult}")
        x = x + 1
    opc = int(input("Deseja continuar \n""1 para sim\n""2 para não: "))
3