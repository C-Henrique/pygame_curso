from typing import Any
import pygame
import os.path
from pygame.locals import *
from sys import exit

pygame.init()

largura: int = 640
altura: int = 480
dirname = os.path.dirname(__file__) or '.'
cor_tela = (0, 0, 0)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')


class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        for i in range(1, 11):
            self.sprites.append(pygame.image.load(
                f'{dirname}/img/attack_{i}.png'))

        self.ataul = 0
        self.image = self.sprites[self.ataul]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        self.animar = False

    def update(self) -> None:
        if self.animar == True:
            self.ataul = self.ataul+ 0.19
            if self.ataul >= len(self.sprites):
                self.ataul = 0
                self.animar = False
                
            self.image = self.sprites[int(self.ataul)]
            self.image = pygame.transform.scale(self.image, (128*3, 64*3))
    
    def atacar(self):
        self.animar = True



todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)
relogio = pygame.time.Clock()
while True:
    tela.fill(cor_tela)
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()
        

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
