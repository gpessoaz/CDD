n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))

media = (n1+n2+n3)/3

if media>=7.0:
    print("Aprovado por média")
elif(media>=4.0):
    print("Recuperação")
else:
    print("Reprovado")

