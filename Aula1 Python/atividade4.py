numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = int(input("Qual Operação deseja fazer? \n"
                     "1 - soma\n"
                     "2 - subtração\n"
                     "3 - multiplicação\n"
                     "4 - divisao"))
if operacao == 1:
    calculo = numero1 + numero2
    print("O resultado da sua soma é ",calculo)
elif operacao == 2:
    calculo = numero1 - numero2
    print("O resultado da sua subtração é: ", calculo)
elif operacao == 3:
    calculo = numero1 * numero2
    print("O resultado da sua multiplicação é: ", calculo)
elif operacao == 4:
    calculo = numero1 / numero2
    print("O resultado da sua divisao é: ", calculo)
else:
    "Escolha um número de 1 a 4!"
