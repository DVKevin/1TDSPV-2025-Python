#Escreva um algoritmo para ler o nome de 2 times e o 
#número de gols marcados em uma partida. Escrever o nome 
#do vencedor. Caso não haja vencedor deverá ser impresso a
#palavra EMPATE.

gols_a = int(input("gols do time A: "))
gols_b = int(input("gols do time B: "))


if gols_a > gols_b:
    print(f"time A ganhou: {gols_a} X {gols_b}")
else:
    if gols_a < gols_b:
        print(f"Time B ganhou: {gols_a} X {gols_b}")
    else:
        print (f"Os dois times empataram {gols_a} X {gols_b}")