import pygame
import pygame.locals
from random import randrange, random

try:
    pygame.init()
    print("O modulo pygame foi inicializado com sucesso")
except:
    print("O modulo pygame não foi inicializado com sucesso")

altura = 800
largura = 800


relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((altura,largura))
pygame.display.set_caption("Star Field")

class Star:
    def __init__(self):
        self.x = randrange((largura/2)-75,(largura/2)+75)
        self.y = randrange((altura/2)-75,(altura/2)+75)
        self.xStart = self.x
        self.yStart = self.y
        self.radius = 2
        self.speedX = randrange(-30,30)
        self.speedY = randrange(-30,30)

    def show(self):
        r = randrange(50,255)
        g = randrange(50,255)
        b = randrange(50,255)
        pygame.draw.circle(fundo, (r,g,b), [self.x, self.y], self.radius)
        pygame.draw.line(fundo, (r,g,b), [self.xStart, self.yStart], [self.x, self.y])
    
    def move(self):
        self.y += self.speedY
        self.x += self.speedX
        if((self.x < 0 or self.x > largura) and  (self.y < 0 or self.y > altura)):
            self.x = randrange((largura/2)-75,(largura/2)+75)
            self.y = randrange((altura/2)-75,(altura/2)+75)

sky = []
for i in range(300):
    star = Star()
    sky.append(star)

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

    for star in sky:
        star.show()
        star.move()

    pygame.display.update()
    relogio.tick(60)

pygame.quit()