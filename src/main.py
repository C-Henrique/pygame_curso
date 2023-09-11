import pygame
from pygame.locals import *
from random import randint
from sys import exit

pygame.init()

sound_impact = pygame.mixer.Sound('./assets/music/smw_1-up.wav')
sound_impact.set_volume(0.6)

largura = 640
altura = 480

x_cobra = largura/2
y_cobra = altura/2 

velocidade = 1.5
x_controle = velocidade
y_controle = 0 

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0

font = pygame.font.SysFont('gabriola', 40, False, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

lista_cobra = []
comprimento_inicial =5
morreu = False

def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (xey[0],xey[1], 20,20))

def reiniciar_jogo():
    global pontos,comprimento_inicial,x_cobra,y_cobra,lista_cabeca,lista_cobra,x_maca,y_maca,morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura/2
    y_cobra = altura/2
    lista_cabeca = []
    lista_cobra = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False


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
        sound_impact.play()
    
    lista_cabeca = []

    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('Arial',20,True,True)
        msg = 'Game over! Pressione a tecla R para jogar novamente.'

        texto_formatado = fonte2.render(msg, True,(0,0,0))
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado,ret_texto)
            pygame.display.update()
    
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra)> comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    

    tela.blit(texto_formatado,(430,40))
    pygame.display.update()