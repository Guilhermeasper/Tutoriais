import pygame
import pygame.locals
import os
from random import randrange, random

try:
    pygame.init()
    print("O modulo pygame foi inicializado com sucesso")
except:
    print("O modulo pygame não foi inicializado com sucesso")

altura = 490
largura = 310
relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tetris")
current_path = os.path.dirname(__file__)  # Where your .py file is located
image_path = os.path.join(current_path, 'imagens')  # The image folder path
black_block = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'black.png')).convert(), (30, 30))
yellow_block = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'yellow.png')).convert(), (30, 30))
blue_block = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'blue.png')).convert(), (30, 30))

true = True

i = [[0, 1],
     [0, 1],
     [0, 1],
     [0, 1]]
j = [[0, 1],
     [0, 1],
     [1, 1]]
l = [[1, 0],
     [1, 0],
     [1, 1]]
o = [[1, 1],
     [1, 1]]
s = [[0, 1, 1],
     [1, 1, 0]]
t = [[0, 1, 0],
     [1, 1, 1]]
z = [[1, 1, 0],
     [0, 1, 1]]

tetriminos = [i, j, l, o, s, t, z]


class Tetrimino:
    choice = randrange(7)
    piece = tetriminos[choice]

    def __init__(self):
        self.tetriminos = tetriminos
        self.x = 0
        self.y = 0
        self.speed = 30
        self.piece = self.tetriminos[randrange(7)]


grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 1]]

# grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
piece = [[]]


def turn(p):
    turned_piece = []
    for j in range(len(p[0]) - 1, -1, -1):
        temp = []
        for i in range(len(p)):
            temp.append(p[i][j])
        turned_piece.append(temp)
    return turned_piece


pygame.time.set_timer(pygame.USEREVENT + 1, 500)
tetris = Tetrimino()
while true:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 1:
            pos = tetris.y + 1
            for i in range(len(piece)):
                for j in range(len(piece[i])):
                    if piece[i][j] + grid[pos + i][tetris.x + j] > 1:
                        pos = tetris.y
            if pos == tetris.y:
                for i in range(len(piece)):
                    for j in range(len(piece[i])):
                        if piece[i][j] == 1:
                            grid[tetris.y + i][tetris.x + j] = 1
                tetris = Tetrimino()
                piece = tetris.piece
            else:
                tetris.y = pos

        if event.type == pygame.QUIT:
            true = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tetris = Tetrimino()
                piece = tetris.piece
                print(tetris.choice)
                print(tetris.piece)
            if event.key == pygame.K_UP:
                piece = turn(piece)
            if event.key == pygame.K_LEFT:
                tetris.x -= 1
            if event.key == pygame.K_RIGHT:
                tetris.x += 1
            if event.key == pygame.K_a:
                for j in range(16):
                    for i in range(10):
                        print(grid[j][i], end=" ")
                    print("")
                print("------------------------------------------------")
                for i in range(len(piece)):
                    for j in range(len(piece[i])):
                        print(tetris.y+i, tetris.x+j)

    fundo.fill((0, 0, 0))
    for i in range(10):
        for j in range(16):
            fundo.blit(black_block, (5 + i * 30, 5 + j * 30))
            if grid[j][i] == 1:
                fundo.blit(blue_block, (5 + i * 30, 5 + j * 30))
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                fundo.blit(yellow_block, (5 + (tetris.x + j) * 30, 5 + (tetris.y + i) * 30))

    pygame.display.update()
    relogio.tick(5)

pygame.quit()
