import math

title = '''
======== MENU ========
== 1 - SOMAR        ==
== 2 - SUBTRAIR     ==
== 3 - MULTIPLICAR  ==
== 4 - DIVIDIR      ==
== 5 - SAIR         ==
======================
'''
menu = {1:"Somar",2:"Subtrair",3:"Multiplicar",4:"Dividir",5:"Sair"}
opcao = 0
while opcao != 5:
    print(f'{title}')
    opcao = menu.get(int(input("Qual opção deseja? ")))
    if opcao == "Sair":
        print(f'Até a próxima!')
        break
    numero_um = int(input("Digite seu primeiro número: "))
    numero_dois = int(input("Digite seu segundo número: "))
    if opcao == "Somar":
        print(f'O resultado de sua Soma é: {numero_um + numero_dois}')
    elif opcao == "Subtrair":
        print(f'O resultado de sua Subtração é: {numero_um - numero_dois}')
    elif opcao == "Multiplicar":
        print(f'O resultado de sua Multiplicação é: {numero_um * numero_dois}')
    elif opcao == "Dividir":
        print(f'O resultado de sua Divisão é: {numero_um / numero_dois:.2f}')
        
