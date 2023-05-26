#jogo da velha

jogo_da_velha = ['','',''],['','',''],['','','']

def menu():
    while continuar:
        continuar = int(input('0 - Sair \n 1 - Jogar novamente'))

def jogo():
    jogada = 0
    while True:

        for list in jogo_da_velha:print(f'{list}')
    
        opção_x = input('Digite linha e coluna de onde você deseja colocar o X')
    
        if opção_x = 