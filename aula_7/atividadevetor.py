numero1 = []
numero2 = []
somanumeros = []

pergunta = int(input("Quantas duplas de numeros deseja cadastrar?"))

for x in range(pergunta):
    numero1.append(int(input("Digite o primeiro número.")))
    numero2.append(int(input("Digite o segundo número")))
    somanumeros.append(numero1[x]+numero2[x])

print(f"{numero1}\n{numero2}\n{somanumeros}")