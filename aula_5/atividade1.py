while True:
    nota1 = float(input("Digite a primeira nota: "))
    nota1bool = nota1 >= 0 and nota1 <= 10
    if nota1bool:
        print("Nota Registrada")
    else:
        while nota1bool == False:
            nota1 = float(input("Digite a primeira nota de 0 a 10: "))
            nota1bool = nota1 >= 0 and nota1 <= 10
        print("Nota Registrada")

    nota2 = float(input("Digite a segunda nota: "))
    nota2bool = nota2 >= 0 and nota2 <= 10

    if nota2bool:
        print("Nota Registrada")
    else:
        while nota2bool == False:
            nota2 = float(input("Digite a segunda nota de 0 a 10: "))
            nota2bool = nota2 >= 0 and nota2 <= 10
        print("Nota Registrada")

    media = (nota1 + nota2) / 2

    print(media)

    continuar = str(input("Deseja continuar? S/N:")).upper()
    if continuar == "N":
        break
