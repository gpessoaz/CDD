peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura**2
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 < imc < 25:
    print("Peso ideal")
elif 25.0 <= imc < 30:
    print("Levemente acima do peso")
elif 30.0 <= imc < 35:
    print("Obeso I")
elif 35.0 <= imc < 40:
    print("Obeso II")
else:
    print("Obeso III")