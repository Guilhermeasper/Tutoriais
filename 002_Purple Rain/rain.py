import pygame
import pygame.locals
from random import randrange, random

try:
    pygame.init()
    print("O modulo pygame foi inicializado com sucesso")
except:
    print("O modulo pygame não foi inicializado com sucesso")

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Purple Rain")

class Drop:
    def __init__(self):
        self.x = randrange(0,1280)
        self.y = randrange(0,720)
        self.size = randrange(3,8)
        self.speed = self.size

    def show(self):
        pygame.draw.rect(fundo, (128,0,128), [self.x, self.y, 1, self.size])
    
    def move(self, mouse):
        self.y += self.speed
        if(self.y >= 720 ):
            self.x = randrange(0,1280)
            self.y = 0

true = True
rain = []
for i in range(2000):
    drop = Drop()
    rain.append(drop)
counter = 0

while true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                true = False
    if 80 <= counter <= 83 or 86 <= counter <= 89:
        fundo.fill((255,255,255))
    else:
        fundo.fill((0,0,0))
    if counter > 89:
        counter = 0
    counter += 1

    for drop in rain:
        drop.show()
        mouse = pygame.mouse.get_pos()
        drop.move(mouse)
    pygame.display.update()
    relogio.tick(30)

pygame.quit()
