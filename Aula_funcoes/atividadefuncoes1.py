import os
from time import sleep

menu = '''
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    5 - Sair
    '''
def interface(x):
    print(f'''
    ===========================================
                    calculadora
    ===========================================
    {x}
    ===========================================
    ===========================================
    ''')
def soma(num1,num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def divisao(num1,num2):
    return num1/num2

def multiplicacao(num1,num2):
    return num1*num2


while True:
    interface(menu)
    opcao = int(input(f'Digite a sua opção: '))

    if opcao == 5:
        break

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    if opcao == 1:
        print(soma(num1,num2))
    elif opcao == 2:
        print(divisao(num1, num2))
    elif opcao == 3:
        print(subtracao(num1, num2))
    elif opcao == 4:
        print(multiplicacao(num1, num2))

