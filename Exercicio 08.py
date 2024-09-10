tm1 = input ("Nome do time 1:")
gt1 = int(input(f"Digite quantos gols o {tm1} fez: "))
tm2 = input("Nome do time 2:")
gt2 = int(input(f"Digite quantos gols o {tm2} fez: "))

if gt1 == gt2:
    print("Partida Empatada")
elif gt1 > gt2:
    print(f"2 {tm1} venceu")
else:
    print(f"0 {tm2} venceu")
