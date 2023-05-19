## IMPORTS
import random
import pygame as pg
from pygame.locals import *

# CORES DO JOGO

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# SETUP DA TELA DO JOGO

window = pg.display.set_mode((1000, 600))

# Iniciando fonte do jogo

pg.font.init()

# Fonte e tamanho

font = pg.font.SysFont('Courier New', 50)
font_rb = pg.font.SysFont('Courier New', 30)

pg.display.set_caption("Jogo da Forca - by HuggsF")

palavras = ["POLTRONA", "DESENVOLVEDOR", "FRUTA", "VIDRAÇA", "CACHORRO", "VIDA", "PARALELEPIPEDO", "CRAVO", "MONTANHA",
            "ROSA"]
tentativas_de_letras = [' ', '-']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chance = 0
letra = ''
click_last_status = False


def desenho_da_forca(window, chance):
    pg.draw.rect(window, BRANCO, (50, 450, 300, 30))
    pg.draw.line(window, BRANCO, (150, 450), (150, 100), 5)
    pg.draw.line(window, BRANCO, (150, 100), (250, 100), 5)
    pg.draw.line(window, BRANCO, (250, 100), (250, 150), 5)
    if chance >= 1:
        pg.draw.circle(window, BRANCO, (250, 175), 25, 5)
    if chance >= 2:
        pg.draw.line(window, BRANCO, (250, 200), (250, 300), 5)
    if chance >= 3:
        pg.draw.line(window, BRANCO, (250, 300), (225, 350), 5)
    if chance >= 4:
        pg.draw.line(window, BRANCO, (150, 100), (250, 100), 5)
    if chance >= 5:
        pg.draw.line(window, BRANCO, (250, 300), (275, 350), 5)
    if chance == 6:
        pg.draw.line(window, BRANCO, (250, 225), (225, 250), 5)
    if chance == 7:
        pg.draw.line(window, BRANCO, (250, 225), (275, 250), 5)


def desenho_restart_button(window):
    pg.draw.rect(window, BRANCO, (700, 100, 240, 65))
    texto = font_rb.render('Recomeçar', True, PRETO)
    window.blit(texto, (740, 120))


def sortear_palavra(palavras, palavra_escolhida, end_game):
    if end_game == True:
        palavra_n = random.randint(0, len(palavras) - 1)
        palavra_escolhida = palavras[palavra_n]
        end_game = False
    return palavra_escolhida, end_game


def camuflando_palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras):
    palavra_camuflada = palavra_escolhida
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n:n + 1] not in tentativas_de_letras:
            palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], "#")
    return palavra_camuflada


def tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance):
    if letra not in tentativas_de_letras:
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
    elif letra in tentativas_de_letras:
        pass
    return tentativas_de_letras, chance


def palavra_do_jogo(window, palavra_camuflada):
    palavra = font.render(palavra_camuflada, True, BRANCO)
    window.blit(palavra, (200, 500))


def restart_do_jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, x, y):
    cont = 0
    limite = len(palavra_camuflada)
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n] != "#":
            cont += 1
    if cont == limite and click_last_status == False and click[0] == True:
        if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            tentativas_de_letras = [' ', '-']
            end_game = True
            chance = 0
            letra = ' '
    return end_game, chance, tentativas_de_letras, letra


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).upper()
            print(letra)

    # Mouse

    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    # clique do mouse
    click = pg.mouse.get_pressed()

    # Jogo

    desenho_da_forca(window, chance)
    desenho_restart_button(window)
    palavra_escolhida, end_game = sortear_palavra(palavras, palavra_escolhida, end_game)
    palavra_camuflada = camuflando_palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras)
    tentativas_de_letras, chance = tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance)
    end_game, chance, tentativas_de_letras, letra = restart_do_jogo(palavra_camuflada, end_game, chance, letra,
                                                                    tentativas_de_letras, click_last_status, click,
                                                                    mouse_position_x, mouse_position_y)
    palavra_do_jogo(window, palavra_camuflada)

    # Click Last Status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()