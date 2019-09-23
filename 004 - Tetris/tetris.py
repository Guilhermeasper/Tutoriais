import pygame
import pygame.locals
from random import randrange, random

try:
    pygame.init()
    print("O modulo pygame foi inicializado com sucesso")
except:
    print("O modulo pygame não foi inicializado com sucesso")


altura = 500
largura = 320
relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Tetris")

true = True
grid = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,0,0,0,0,0],
        [0,1,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

while true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                true = False
    fundo.fill((0,0,0))
    for i in range(16):
        for j in range(10):
            if grid[i][j] == 1:
                for x in range(30):
                    for y in range(30):
                        fundo.set_at((j*30+x, i*30+y), (255,255,255))

    
    pygame.display.update()
    relogio.tick(30)

pygame.quit()
