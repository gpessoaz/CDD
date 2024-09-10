nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salário = float(input("Digite seu salário: "))
print(f"Olá, {nome}, sua idade é {idade} e seu salário é {salário}")

novosalário = (salário * 1.1)
meses = idade*12

print(f"Houve um aumento de 10% no seu salário {novosalário:.2f}")

print(f"Olá {nome},\n"
      f"voce tem {idade} anos e o seu salário é {novosalário:.2f}"
      f"e voce viveu por {meses}")

