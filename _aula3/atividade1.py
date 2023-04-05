numero_1 = int(input("Digite seu número e eu direi a que mês ele corresponde.\n 1 a 12, ok?"))


if numero_1 > 0 and numero_1 <= 12:
    if numero_1 == 1:
        print("Janeiro.")
    elif numero_1 == 2:
            print("Fevereiro.")
    elif numero_1 == 3:
            print("Março.")
    elif numero_1 == 4:
            print("Abril.")
    elif numero_1 == 5:
            print("Maio.")
    elif numero_1 == 6:
            print("Junho.")
    elif numero_1 == 7:
            print("Julho.")
    elif numero_1 == 8:
            print("Agosto.")
    elif numero_1 == 9:
            print("Setembro.")
    elif numero_1 == 10:
            print("Outubro.")
    elif numero_1 == 11:
            print("Novembro.")
    else:
            print("Dezembro.")
else: print("Digite um número de 1 a 12.")