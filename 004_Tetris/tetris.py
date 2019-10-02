import pygame
import pygame.locals
import os
from random import randrange, random

current_path = os.path.dirname(__file__) # Where your .py file is located
image_path = os.path.join(current_path, 'imagens') # The image folder path

try:
    pygame.init()
    print("O modulo pygame foi inicializado com sucesso")
except:
    print("O modulo pygame não foi inicializado com sucesso")


altura = 1200
largura = 720
relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tetris")

tetrimino_i = pygame.image.load(os.path.join(image_path, 'i.png'))
tetrimino_j = pygame.image.load(os.path.join(image_path, 'j.png'))
tetrimino_l = pygame.image.load(os.path.join(image_path, 'l.png'))
tetrimino_o = pygame.image.load(os.path.join(image_path, 'o.png'))
tetrimino_s = pygame.image.load(os.path.join(image_path, 's.png'))
tetrimino_t = pygame.image.load(os.path.join(image_path, 't.png'))
tetrimino_z = pygame.image.load(os.path.join(image_path, 'z.png'))

true = True

counter = 0
while true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False
            break
    fundo.fill((255,255,255))
    fundo.blit(tetrimino_z, (0,counter))
    counter += 50
    pygame.display.update()
    relogio.tick(5)

pygame.quit()
