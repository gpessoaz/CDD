pin = 1234
senha =  int(input("Digite sua senha: "))
tentativa = 1
while senha != pin and tentativa<3:
    senha = int(input(f"senha inválida"
                      f"você tem {3-tentativa}\n"
                      f"Digite sua senha: "))
    tentativa+=1
if tentativa== 3 and senha!=pin:
    print("Senha bloqueada")
else:
    print("Retire seu cartão")