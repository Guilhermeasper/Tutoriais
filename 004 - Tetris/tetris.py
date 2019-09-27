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

def generate_random_piece():
    pos = [[2,4],[-1,-1], [-1,-1], [-1,-1]]

    piece = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]

    frst = randrange(0,3)

    if frst == 0:
        piece[1][4] = 1
        pos[1][0] = 1
        pos[1][1] = 4
    elif frst == 1:
        piece[2][5] = 1
        pos[1][0] = 2
        pos[1][1] = 5
    elif frst == 2:
        piece[2][4] = 1
        pos[1][0] = 2
        pos[1][1] = 4
    else:
        piece[2][3] = 1
        pos[1][0] = 2
        pos[1][1] = 3

    selected = False
    seletor = randrange(0,1)

    while(not selected):
        scnd = randrange(0,3)

        if scnd == 0 and piece[pos[seletor][0]-1] [pos[seletor][1]] != 1:
            piece[pos[seletor][0]-1] [pos[seletor][1]] = 1
            pos[2][0] = pos[seletor] [0]-1
            pos[2][1] = pos[seletor] [1]
            selected = true
        elif scnd == 1 and piece[pos[seletor][0]] [pos[seletor][1]+1] != 1:
            piece[pos[seletor][0]] [pos[seletor][1]+1] = 1
            pos[2][0] = pos[seletor] [0]-1
            pos[2][1] = pos[seletor] [1]
            selected = true
        elif scnd == 2 and piece[pos[seletor][0]+1] [pos[seletor][1]] != 1:
            piece[pos[seletor][0]+1] [pos[seletor][1]] = 1
            pos[2][0] = pos[seletor] [0]-1
            pos[2][1] = pos[seletor] [1]
            selected = true
        elif scnd == 3 and piece[pos[seletor][0]] [pos[seletor][1]-1] != 1:
            piece[pos[seletor][0]] [pos[seletor][1]-1] = 1
            pos[2][0] = pos[seletor] [0]-1
            pos[2][1] = pos[seletor] [1]
            selected = true
    
    selected = False
    seletor = randrange(0,2)

    while(not selected):
        scnd = randrange(0,3)

        if scnd == 0 and piece[pos[seletor][0]-1] [pos[seletor][1]] != 1:
            piece[pos[seletor][0]-1] [pos[seletor][1]] = 1
            pos[2][0] = pos[seletor] [0]-1
            pos[2][1] = pos[seletor] [1]
            selected = true
        elif scnd == 1 and piece[pos[seletor][0]] [pos[seletor][1]+1] != 1:
            piece[pos[seletor][0]] [pos[seletor][1]+1] = 1
            pos[2][0] = pos[seletor] [0]-1
            pos[2][1] = pos[seletor] [1]
            selected = true
        elif scnd == 2 and piece[pos[seletor][0]+1] [pos[seletor][1]] != 1:
            piece[pos[seletor][0]+1] [pos[seletor][1]] = 1
            pos[2][0] = pos[seletor] [0]-1
            pos[2][1] = pos[seletor] [1]
            selected = true
        elif scnd == 3 and piece[pos[seletor][0]] [pos[seletor][1]-1] != 1:
            piece[pos[seletor][0]] [pos[seletor][1]-1] = 1
            pos[2][0] = pos[seletor] [0]-1
            pos[2][1] = pos[seletor] [1]
            selected = true

    for line in piece:
        print(line)
    print("")


grid = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

while true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                generate_random_piece()
            if event.key == pygame.K_UP:
                for i in range(16):
                    for j in range(10):
                        if grid[i][j] == 1:
                            grid[i][j] = 0
                            grid[i-1][j] = 1
            if event.key == pygame.K_DOWN:
                for i in range(15,0,-1):
                    for j in range(9,0,-1):
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
                for j in range(9,0,-1):
                    for i in range(16):
                        if grid[i][j] == 1:
                            grid[i][j] = 0
                            grid[i][j+1] = 1
    fundo.fill((120,120,120))
    for i in range(16):
        for j in range(10):
            if grid[i][j] == 1 or grid[i][j] == 2:
                for x in range(1,28):
                    for y in range(1,28):
                        fundo.set_at((j*30+x, i*30+y), (0,255,255))
        for i in range(15,0,-1):
            for j in range(9,0,-1):
                if i == 15 and grid[i][j] == 1:
                    for i in range(16):
                        for j in range(10):
                            if grid[i][j] == 1:
                                grid[i][j] = 2
    for i in range(15,0,-1):
        for j in range(9,0,-1):
            if grid[i][j] == 1:
                grid[i][j] = 0
                grid[i+1][j] = 1
                
    

    
    pygame.display.update()
    relogio.tick(5)

pygame.quit()
