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


altura = 520
largura = 302
relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tetris")

tetrimino_i = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'i.png')).convert(), (120,30))
tetrimino_i.set_colorkey( (0,0, 0))
tetrimino_j = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'j.png')).convert(), (90,60))
tetrimino_j.set_colorkey( (0,0, 0))
tetrimino_l = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'l.png')).convert(), (90,60))
tetrimino_l.set_colorkey( (0,0, 0))
tetrimino_o = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'o.png')).convert(), (59,60))
tetrimino_o.set_colorkey( (0,0, 0))
tetrimino_s = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 's.png')).convert(), (90,60))
tetrimino_s.set_colorkey( (0,0, 0))
tetrimino_t = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 't.png')).convert(), (90,60))
tetrimino_t.set_colorkey( (0,0, 0))
tetrimino_z = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'z.png')).convert(), (90,60))
tetrimino_z.set_colorkey( (0,0, 0))

true = True

counter = 120
while true:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tetrimino_i = pygame.transform.chop(tetrimino_i, (90,0,120,30))
        if event.type == pygame.QUIT:
            true = False
            break
    fundo.fill((255,255,255))
    for i in range(17):
        pygame.draw.line(fundo, (0,0,0), (0,i*30),(largura,i*30))
    for i in range(11):
        pygame.draw.line(fundo, (0,0,0), (i*30,0),(i*30,altura-40))
    
    fundo.blit(tetrimino_i, (30,30))
    fundo.blit(tetrimino_j, (60,90))
    fundo.blit(tetrimino_l, (90,150))
    fundo.blit(tetrimino_o, (120,210))
    fundo.blit(tetrimino_s, (150,270))
    fundo.blit(tetrimino_t, (180,330))
    fundo.blit(tetrimino_z, (210,390))
    counter += 30
    pygame.display.update()
    relogio.tick(2)

pygame.quit()
