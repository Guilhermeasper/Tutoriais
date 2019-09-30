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
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tetris")

true = True


def generate_random_piece():
    pos = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]

    piece = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    pos[0][0] = randrange(0, 4)
    pos[0][1] = randrange(0, 10)

    piece[pos[0][0]][pos[0][1]] = 1
    selected = False
    while(not selected):
        frst = randrange(0, 4)

        if frst == 0 and pos[0][0]-1 >= 0:
            piece[pos[0][0]-1][pos[0][1]] = 1
            pos[1][0] = pos[0][0]-1
            pos[1][1] = pos[0][1]
            selected = True
        elif frst == 1 and pos[0][1]+1 <= 9:
            piece[pos[0][0]][pos[0][1]+1] = 1
            pos[1][0] = pos[0][0]
            pos[1][1] = pos[0][1]+1
            selected = True
        elif frst == 2 and pos[0][0]+1 <= 4:
            piece[pos[0][0]+1][pos[0][1]] = 1
            pos[1][0] = pos[0][0]+1
            pos[1][1] = pos[0][1]
            selected = True
        elif frst == 3 and pos[0][1]-1 >=0:
            piece[pos[0][0]][pos[0][1]-1] = 1
            pos[1][0] = pos[0][0]
            pos[1][1] = pos[0][1]-1
            selected = True

    selected = False
    seletor = randrange(0, 2)

    while(not selected):
        scnd = randrange(0, 4)

        if pos[seletor][0]-1 >= 0 and scnd == 0 and piece[pos[seletor][0]-1][pos[seletor][1]] != 1:
            piece[pos[seletor][0]-1][pos[seletor][1]] = 1
            pos[2][0] = pos[seletor][0]-1
            pos[2][1] = pos[seletor][1]
            selected = True
        elif pos[seletor][1]+1 <= 9 and scnd == 1 and piece[pos[seletor][0]][pos[seletor][1]+1] != 1:
            piece[pos[seletor][0]][pos[seletor][1]+1] = 1
            pos[2][0] = pos[seletor][0]
            pos[2][1] = pos[seletor][1]+1
            selected = True
        elif pos[seletor][0]+1 <= 4 and scnd == 2 and piece[pos[seletor][0]+1][pos[seletor][1]] != 1:
            piece[pos[seletor][0]+1][pos[seletor][1]] = 1
            pos[2][0] = pos[seletor][0]+1
            pos[2][1] = pos[seletor][1]
            selected = True
        elif pos[seletor][1]-1 >= 0 and scnd == 3 and piece[pos[seletor][0]][pos[seletor][1]-1] != 1:
            piece[pos[seletor][0]][pos[seletor][1]-1] = 1
            pos[2][0] = pos[seletor][0]
            pos[2][1] = pos[seletor][1]-1
            selected = True

    selected = False
    seletor = randrange(0, 3)

    while(not selected):
        scnd = randrange(0, 4)

        if pos[seletor][0]-1 >= 0 and scnd == 0 and piece[pos[seletor][0]-1][pos[seletor][1]] != 1:
            piece[pos[seletor][0]-1][pos[seletor][1]] = 1
            pos[2][0] = pos[seletor][0]-1
            pos[2][1] = pos[seletor][1]
            selected = True
        elif pos[seletor][1]+1 <= 9 and scnd == 1 and piece[pos[seletor][0]][pos[seletor][1]+1] != 1:
            piece[pos[seletor][0]][pos[seletor][1]+1] = 1
            pos[2][0] = pos[seletor][0]
            pos[2][1] = pos[seletor][1]+1
            selected = True
        elif pos[seletor][0]+1 <= 4 and scnd == 2 and piece[pos[seletor][0]+1][pos[seletor][1]] != 1:
            piece[pos[seletor][0]+1][pos[seletor][1]] = 1
            pos[2][0] = pos[seletor][0]+1
            pos[2][1] = pos[seletor][1]
            selected = True
        elif pos[seletor][1]-1 >= 0 and scnd == 3 and piece[pos[seletor][0]][pos[seletor][1]-1] != 1:
            piece[pos[seletor][0]][pos[seletor][1]-1] = 1
            pos[2][0] = pos[seletor][0]
            pos[2][1] = pos[seletor][1]-1
            selected = True

    for line in piece:
        print(line)
    print("")
    return piece


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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

while true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new = generate_random_piece()
            for i in range(5):
                for j in range(10):
                    grid[i+1][j] = new[i][j]
            if event.key == pygame.K_UP:
                for i in range(16):
                    for j in range(10):
                        if grid[i][j] == 1:
                            grid[i][j] = 0
                            grid[i-1][j] = 1
            if event.key == pygame.K_DOWN:
                for i in range(15, -1, -1):
                    for j in range(9, -1, -1):
                        if grid[i][j] == 1:
                            grid[i][j] = 0
                            grid[i+1][j] = 1
            if event.key == pygame.K_LEFT:
                for j in range(10):
                    for i in range(16):
                        if grid[i][j] == 1:
                            grid[i][j] = 0
                            grid[i][j-1] = 1
            if event.key == pygame.K_RIGHT:
                for j in range(9, -1, -1):
                    for i in range(16):
                        if grid[i][j] == 1:
                            grid[i][j] = 0
                            grid[i][j+1] = 1
    fundo.fill((120, 120, 120))
    for i in range(16):
        for j in range(10):
            if grid[i][j] == 1 or grid[i][j] == 2:
                for x in range(1, 29):
                    for y in range(1, 29):
                        fundo.set_at((j*30+x, i*30+y), (0, 255, 255))
    for i in range(15, -1, -1):
        for j in range(9, -1, -1):
            if i == 15 and grid[i][j] == 1:
                for x in range(16):
                    for y in range(10):
                        if grid[x][y] == 1:
                            grid[x][y] = 2
    # for i in range(15, -1, -1):
    #     for j in range(9, -1, -1):
    #         if grid[i][j] == 1:
    #             grid[i][j] = 0
    #             grid[i+1][j] = 1
    
    pygame.display.update()
    relogio.tick(30)

pygame.quit()
