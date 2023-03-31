nota_1 = float(input("Digite a Primeira Nota"))
nota_2 = float(input("Digite a Segunda Nota"))
nota_3 = float(input("Digite a Terceira Nota"))
media = float((nota_1 + nota_2 + nota_3)/ 3)

if (media >= 7): print("Aprovado")
elif (media >= 4 and media < 7): print("Em recuperação")
else: print("Reprovado")

