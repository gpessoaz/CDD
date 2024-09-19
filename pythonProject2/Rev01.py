A = int(input("Digite A: "))
B = int(input("Digite B: "))
C = int(input("Digite C: "))

soma = A + B

if soma < C:
    print("A soma é menor que C")
elif soma == C:
    print("A soma é igual a C")
else:
    print("A soma é maior que C")