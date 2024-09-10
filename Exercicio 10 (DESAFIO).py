h1 = int(input("Digite a hora da primeira entrada: "))
m1 = int(input("Digite o minuto da primeira entrada: "))
if 0 <= h1 <= 24 and 0 <= m1 < 60:
    h2 = int(input("Digite a hora da segunda entrada: "))
    m2 = int(input("Digite o minuto da segunda entrada: "))
    if 0 <= h2 <= 24 and 0 <= m2 < 60:
        if h1 > 12:
            h1 -= 12
        if h2 > 12:
            h2 -= 12

        somamin = m1 + m2
        somahoras = (h1 + h2)
        if somamin >= 60:
            somamin -=60
            somahoras +=1
        if somahoras > 12:
            somahoras -=12
    print(somahoras, somamin)
else:
    print("Hora ou Minuto inválido")



