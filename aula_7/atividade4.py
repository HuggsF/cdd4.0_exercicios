lista = []
maiorNumero = 0
somaTotal = 0
count = 0


for x in range(5):
    numero = int(input("Digite seu numero: "))
    lista.append(numero)
    somaTotal += numero

media = somaTotal/5

for x in range(5):
    if lista[x]%2 == 0:
        print(f"{lista[x]}")

for x in range(5):
    if lista[x] > maiorNumero:
        maiorNumero = lista[x]
print(f"{maiorNumero}")

for x in range(5):
    if lista[x] > media:
        count+=1

print(f"A média é {media} e {count} números em sua lista são maiores que ela.")