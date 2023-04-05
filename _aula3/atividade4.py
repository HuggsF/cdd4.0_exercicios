numero = int(input("Digite seu número."))

for x in range(1,numero+1):
    if(x%2 != 0):
        print(x, " é impar.")
    else:
        continue
