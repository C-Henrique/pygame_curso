import pygame
from pygame.locals import *
from random import randint
from sys import exit

pygame.init()

largura = 640
altura = 480

x_blue = largura/2
y_blue = 0 

x_red = randint(40, 600)
y_red = randint(50, 430)

velocidade = 5
pontos = 0

font = pygame.font.SysFont('gabriola', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
while True:
    relogio.tick(120)
    tela.fill((0,0,0))
    msg = f'Pontos: {pontos}'
    texto_formatado = font.render(msg,True, (255,255,255))

    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
        ''' 
    if pygame.key.get_pressed()[K_a]:
        x_blue = x_blue - velocidade
    if  pygame.key.get_pressed()[K_d]:
        x_blue = x_blue + velocidade
    if  pygame.key.get_pressed()[K_w]:
        y_blue = y_blue - velocidade
    if  pygame.key.get_pressed()[K_s]:
        y_blue = y_blue + velocidade
    ret_azul = pygame.draw.rect(tela,(255,0,0),(x_blue,y_blue,40,40))
    ret_vermelho =  pygame.draw.rect(tela,(0,60,120),(x_red,y_red,40,40))
    
    if ret_vermelho.colliderect(ret_azul):
        x_red = randint(40, 600)
        y_red = randint(50, 430)
        pontos = pontos +1
    
    tela.blit(texto_formatado,(430,40))
    pygame.display.update()