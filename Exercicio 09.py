litros = float(input("Quantos litros voce quer?"))
tipo = input("G-GASOLINA e E-ETANOL: ")
if tipo == "G" or "g":
    preco = litros * 5.8
    print("O valor é:", preco)
elif tipo == "e" or "E":
    preco = litros * 4.9
    print("O valor é:", preco)

else:
    print("Tipo invalido")

