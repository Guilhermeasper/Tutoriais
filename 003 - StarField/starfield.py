import pygame
import pygame.locals
from random import randrange, random

try:
    pygame.init()
    print("O modulo pygame foi inicializado com sucesso")
except:
    print("O modulo pygame não foi inicializado com sucesso")

altura = 600
largura = 600

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((altura,largura))
pygame.display.set_caption("Star Field")

class Drop:
    def __init__(self):
        self.x = randrange((largura/2)-50,(largura/2)+50)
        self.y = randrange((altura/2)-50,(altura/2)+50)
        self.radius = 1
        self.speed = 2

    def show(self):
        pygame.draw.rect(fundo, (255,255,255), tuple(self.x, self.y), self.radius)
    
    def move(self, mouse):
        self.y += self.speed
        if(self.y >= 720 ):
            self.x = randrange(0,1280)
            self.y = 0


true = True
while true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                true = False
    fundo.fill((0,0,0))

    pygame.display.update()
    relogio.tick(30)