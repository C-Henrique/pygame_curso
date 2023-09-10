import pygame
from pygame.locals import *
from random import randint
from sys import exit

pygame.init()

largura = 640
altura = 480

x_cobra = largura/2
y_cobra = 0 

velocidade = 1.5
x_controle = velocidade
y_controle = 0 

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0

font = pygame.font.SysFont('gabriola', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

lista_cobra = []
comprimento_inicial =5

def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (xey[0],xey[1], 20,20))

while True:
    relogio.tick(120)
    tela.fill((255,255,255))
    msg = f'Pontos: {pontos}'
    texto_formatado = font.render(msg,True, (0,0,0))

    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0 
                    y_controle = velocidade
    ''' 
    if pygame.key.get_pressed()[K_a]:
        x_cobra = x_cobra - velocidade
    if  pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra + velocidade
    if  pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra - velocidade
    if  pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra + velocidade
    '''

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20))
    maca =  pygame.draw.rect(tela,(255,0,0),(x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos +1
        comprimento_inicial = comprimento_inicial + 1
    
    lista_cabeca = []

    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)
    if len(lista_cobra)> comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    

    tela.blit(texto_formatado,(430,40))
    pygame.display.update()