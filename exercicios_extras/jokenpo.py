import random

jogo = ["Pedra", "Papel", "Tesoura"]
jogada_do_computador = random.choice(jogo)

escolha_jogador = input('Pedra, Papel ou Tesoura? ').title()
print(f'''A jogada do computador foi: {jogada_do_computador}.
A sua jogada foi {escolha_jogador}.''')
match escolha_jogador:
    case 'Pedra':
        if jogada_do_computador == 'Tesoura':
            print(f'Você venceu!')
        elif jogada_do_computador =='Pedra':
            print(f'Empate!')
        else:
            print(f'Você perdeu!')
    case 'Papel':
        if jogada_do_computador == 'Tesoura':
            print(f'Você perdeu!')
        elif jogada_do_computador =='Pedra':
            print(f'Você venceu!')
        else:
            print(f'Empate!')
    case 'Tesoura':
        if jogada_do_computador == 'Tesoura':
            print(f'Empate!')
        elif jogada_do_computador =='Pedra':
            print(f'Você perdeu!')
        else:
            print(f'Você venceu!')
            
