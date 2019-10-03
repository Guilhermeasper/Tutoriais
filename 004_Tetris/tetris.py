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
        if direcao == 'e' and self.x > 0:
            self.x -= 30
        elif direcao == 'r' and self.x < 300-self.piece.get_size()[0]-2:
            self.x += 30
        else:
            self.y += self.speed
            if self.y + self.piece.get_size()[1] > 480:
                self.y -= self.speed

    def rotaciona(self):
        self.piece = pygame.transform.rotate(self.piece, 90)
        if(self.x + self.piece.get_size()[0] > 300):
            self.piece = pygame.transform.rotate(self.piece, -90)
        if(self.y + self.piece.get_size()[1] > 450):
            self.piece = pygame.transform.rotate(self.piece, -90)

    def stop(self):
        if self.y > 450 - self.piece.get_size()[1]:
            self.speed = 0
            return True
        else:
            return False
true = True
blit = False
atual = None
pos_y = 0
pos_x = randrange(0, 180, 30)
speed_y = 30
piece = Tetrimino()
pieces = []
movido = False
while true:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                piece = Tetrimino()
                print(piece.piece.get_size())
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
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        piece.move('')
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        piece.move('e')
        movido = True
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        piece.move('r')
        movido = True
    if not movido:
        piece.move('')
    piece.mostra()
    aux = piece.stop()
    for item in pieces:
        if item.piece.get_rect().colliderect(piece.piece.get_rect()):
            print('Bateu')
            piece.stop()
            pieces.append(piece)
            piece = Tetrimino()
            break
            
    for item in pieces:    
        item.mostra()
    if aux:
        pieces.append(piece)
        piece = Tetrimino()
    pos_y += speed_y
    movido = False
    pygame.display.update()
    relogio.tick(60)
    pygame.time.delay(200)

pygame.quit()
