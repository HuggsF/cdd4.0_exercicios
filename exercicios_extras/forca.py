## jogo da forca
import random

palavras_aleatorias = ["Poltrona","Desenvolvedor","Fruta","Pão","Vidraça","Cachorro","Vida","Paralelepipedo","Cravo","Montanha"]

letras_ja_tentadas = []

jogo_da_forca = random.choice(palavras_aleatorias)

palavra_minuscula = jogo_da_forca.lower()

estado_atual = ["_"]*len(jogo_da_forca)

tentativas = 10

palavra_final = jogo_da_forca

continuar = "N"

while True:

    print(f'{estado_atual}')

    letra = str(input('Digite uma letra.'))

    letras_ja_tentadas.append(letra)
    

    if letra in jogo_da_forca.lower():
        for i in range(len(jogo_da_forca)):
            if letra == jogo_da_forca[i] or letra == palavra_minuscula[i]:
                if i == 0:
                    estado_atual[i] = letra.upper()
                    print(f'Você acertou a letra {letra}! Agora sua palavra está assim:{estado_atual}')
                else:
                    estado_atual[i] = letra
                    print(f'Você acertou a letra {letra}! Agora sua palavra está assim:{estado_atual}')
                
                continuar = input('Você ja sabe qual é a palavra? S/N: ').upper()
                
                if continuar.upper() == "S":
                    tentativa_de_palavra = input('Digite a palavra: ')
                    if tentativa_de_palavra.title() == palavra_final.title():
                        print(f'Parabéns, você ganhou!, sua palavra era {palavra_final}')
                        exit()
    else:
        tentativas -= 1
        print(f'Você errou, restam {tentativas} tentativas!')
            
    if tentativas == 0:
        print(f'Você perdeu!')
        break