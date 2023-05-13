## jogo da forca

import random
import pygame as pg

pg.init()

#CORES DO JOGO

BRANCO = (255,255,255)
PRETO = (0,0,0)

# SETUP DA TELA DO JOGO
window = pg.display.set_mode((1000,600))
# Fonte e tamanho
font = pg.font.SysFont('Courier New', 50)
font_rb = pg.font.SysFont('Courier New', 30)

pg.display.set_caption("Jogo da Forca - by HuggsF")

palavras_aleatorias = ["Poltrona","Desenvolvedor","Fruta","Pão","Vidraça"]

letras_ja_tentadas = []

jogo_da_forca = random.choice(palavras_aleatorias)

end_game = True

palavra_minuscula = jogo_da_forca.lower()

estado_atual = ["_"]*len(jogo_da_forca)

tentativas = 6

palavra_final = jogo_da_forca

continuar = "N"

def desenho_da_forca(window,chance):
    pg.draw.rect(window, PRETO,(0,0,1000,600))
    pg.draw.line(window, BRANCO,(100,500),(100,100),10)
    pg.draw.line(window, BRANCO,(50,500),(150,500),10)
    pg.draw.line(window, BRANCO,(100,100),(300,100),10)
    pg.draw.line(window, BRANCO,(300,100),(300,150),10)
    if tentativas >= 1:
        pg.draw.circle(window,BRANCO,(300,200),50,10)
    if tentativas >= 2:
        pg.draw.line(window,BRANCO,(300,250),(300,350),10)
    if tentativas >= 3:
        pg.draw.line(window,BRANCO,(300,260),(225,350),10)
    if tentativas >= 4:
        pg.draw.line(window,BRANCO,(300,260),(375,350),10)
    if tentativas >= 5:
        pg.draw.line(window,BRANCO,(300,350),(375,450),10)
    if tentativas >= 6:
        pg.draw.line(window,BRANCO,(300,350),(225,450),10)
        
def desenho_restart_button(window):
    pg.draw.rect(window,BRANCO,(700,100,240,65))
    texto = font_rb.render('Recomeçar', True,PRETO)
    window.blit(texto,(740,120))

def sortear_palavra():
    #voltar daqui
    return                 
while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).upper()
            print(letra)
    #jogo
    desenho_da_forca(window,tentativas)
    desenho_restart_button(window)
            
    pg.display.update()

    # print(f'{estado_atual}')

    # letra = str(input('Digite uma letra.'))

    # letras_ja_tentadas.append(letra)
    

    # if letra in jogo_da_forca.lower():
    #     for i in range(len(jogo_da_forca)):
    #         if letra == jogo_da_forca[i] or letra == palavra_minuscula[i]:
    #             if i == 0:
    #                 estado_atual[i] = letra.upper()
    #                 print(f'Você acertou a letra {letra}! Agora sua palavra está assim:{estado_atual}')
    #             else:
    #                 estado_atual[i] = letra
    #                 print(f'Você acertou a letra {letra}! Agora sua palavra está assim:{estado_atual}')
                
    #             continuar = input('Você ja sabe qual é a palavra? S/N: ').upper()
                
    #             if continuar.upper() == "S":
    #                 tentativa_de_palavra = input('Digite a palavra: ')
    #                 if tentativa_de_palavra.title() == palavra_final.title():
    #                     print(f'Parabéns, você ganhou!, sua palavra era {palavra_final}')
    #                     exit()
    # else:
    #     tentativas -= 1
    #     print(f'Você errou, restam {tentativas} tentativas!')
            
    # if tentativas == 0:
    #     print(f'Você perdeu!')
    #     break