import pygame
from pygame.locals import *
from sys import exit

pygame.init();

largura = 640
altura = 480
cor_tela = (0,0,0)
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Sprites')


class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


while True:
    tela.fill(cor_tela)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()