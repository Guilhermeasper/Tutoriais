import pygame
import pygame.locals
import os
from random import randrange, random

current_path = os.path.dirname(__file__)  # Where your .py file is located
image_path = os.path.join(current_path, 'imagens')  # The image folder path

try:
    pygame.init()
    print("O modulo pygame foi inicializado com sucesso")
except:
    print("O modulo pygame não foi inicializado com sucesso")


def load_images():
    i = pygame.transform.scale(pygame.image.load(
        os.path.join(image_path, 'i.png')).convert(), (120, 30))
    j = pygame.transform.scale(pygame.image.load(
        os.path.join(image_path, 'j.png')).convert(), (90, 60))
    l = pygame.transform.scale(pygame.image.load(
        os.path.join(image_path, 'l.png')).convert(), (90, 60))
    o = pygame.transform.scale(pygame.image.load(
        os.path.join(image_path, 'o.png')).convert(), (59, 60))
    s = pygame.transform.scale(pygame.image.load(
        os.path.join(image_path, 's.png')).convert(), (90, 60))
    t = pygame.transform.scale(pygame.image.load(
        os.path.join(image_path, 't.png')).convert(), (90, 60))
    z = pygame.transform.scale(pygame.image.load(
        os.path.join(image_path, 'z.png')).convert(), (90, 60))
    i.set_colorkey((0, 0, 0))
    j.set_colorkey((0, 0, 0))
    l.set_colorkey((0, 0, 0))
    o.set_colorkey((0, 0, 0))
    s.set_colorkey((0, 0, 0))
    t.set_colorkey((0, 0, 0))
    z.set_colorkey((0, 0, 0))
    r = [i, j, l, o, s, t, z]
    return r


altura = 520
largura = 302
relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tetris")


class Tetrimino:
    def __init__(self):
        self.tetriminos = load_images()
        self.x = 0
        self.y = 0
        self.speed = 30
        self.piece = self.tetriminos[randrange(7)]

    def random_tetrimino(self):
        return self.piece

    def mostra(self):
        fundo.blit(self.piece, (self.x, self.y))

    def move(self, direcao):
        if direcao == 'e':
            self.x -= 30
        elif direcao == 'r':
            self.x += 30
        else:
            self.y += self.speed

    def rotaciona(self):
        self.piece = pygame.transform.rotate(self.piece, 90)

    def stop(self):
        if self.y >390:
            self.speed = 0
true = True
blit = False
atual = None
pos_y = 0
pos_x = randrange(0, 180, 30)
speed_y = 30
piece = Tetrimino()
movido = False
while true:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                piece = Tetrimino()
            if event.key == pygame.K_DOWN:
                piece.move('')
            if event.key == pygame.K_UP:
                piece.rotaciona()
        if event.type == pygame.QUIT:
            true = False
            break
    fundo.fill((255,255,255))
    for i in range(17):
        pygame.draw.line(fundo, (0,0,0), (0,i*30),(largura,i*30))
    for i in range(11):
        pygame.draw.line(fundo, (0,0,0), (i*30,0),(i*30,altura-40))
    
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        piece.move('e')
        pygame.display.update()
        movido = True
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        piece.move('r')
        pygame.display.update()
        movido = True
    if not movido:
        piece.move('')
    piece.mostra()
    piece.stop()
    pos_y += speed_y
    movido = False
    pygame.display.update()
    relogio.tick(1)
    #pygame.time.delay(50)

pygame.quit()
