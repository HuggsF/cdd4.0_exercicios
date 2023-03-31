time_1 = int(input("Quantos gols o time1 fez?"))
time_2 = int(input("Quantos gols o time2 fez?"))

if time_1 == time_2 :
    print("Empate")
else:
    if time_1 > time_2 :
        print("TIME 1 VENCEDOR")
    else: print("TIME 2 VENCEDOR")


class Time:
    def __init__(self, nome, gols):
        self.nome = nome
        self.gols = gols

time1 = Time([],[])

time1.nome = input("Qual o nome do time1?")

print(time1.nome)