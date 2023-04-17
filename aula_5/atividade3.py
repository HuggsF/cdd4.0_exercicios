operacao = 5
while operacao == 5:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = int(input(
        " Digite sua operação: \n 1 - soma \n 2 - subtração \n 3 - multiplicação \n 4 - divisao \n 5 - digitar novo número \n 6 - sair."))

class Calculadora:
    def soma(x,y):
        return x+y
    def subtracao(x,y):
        return x-y
    def multiplicacao(x,y):
        return x*y
    def divisao(x,y):
        return x/y


print(Calculadora.get(operacao))