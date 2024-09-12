import pygame
from sys import exit
import random
import time

image_filename1 = 'dog.png'
image_filename2 = 'bush.png'
image_filename3 = 'flag.png'
image_filename4 = 'scary_dog.png'
run = True
pygame.init()
screen = pygame.display.set_mode((1400, 700))
pygame.display.set_caption("moving with arrows")

img1 = pygame.image.load(image_filename1)
img1 = pygame.transform.scale(img1, (2 * (1400 / 50), 4 * (700 / 25)))
img2 = pygame.image.load(image_filename2)
img2 = pygame.transform.scale(img2, (2 * (1400 / 50), 2 * (700 / 25)))
img3 = pygame.image.load(image_filename3)
img3 = pygame.transform.scale(img3, (4 * (1400 / 50), 3 * (700 / 25)))
img4 = pygame.image.load(image_filename4)
img4 = pygame.transform.scale(img4, (3 * (1400 / 50), 1 * (700 / 25)))
x = 0
y = 0
bush_list = []
bomb_list = []
board = [[0 for i in range(50)] for j in range(25)]
for i in range(20):
    random_row = random.randint(0, 23)
    random_col = random.randint(0, 48)
    if board[random_row][random_col] == 0:
        bush_list.append((random_row, random_col))
        board[random_row][random_col] = 2
    random_row = random.randint(0, 23)
    random_col = random.randint(0, 48)
    if board[random_row][random_col] == 0:
        bomb_list.append((random_row, random_col))
        board[random_row][random_col] = 4
board[0][0] = 1
board[22][46] = 3

player = []
flag = []
for i in range(21, 25):
    for j in range(46, 50):
        flag.append((i, j))
for i in board:
    print(i)
print(bush_list)
while True:
    screen.fill("dark green")
    screen.blit(img3, (46 * (700 / 25), 21 * (1400 / 50)))
    for i in bush_list:
        board[i[0]][i[1]] = 2
        screen.blit(img2, (i[1] * (1400 / 50), i[0] * (700 / 25)))
    for i in bomb_list:
        board[i[0]][i[1]] = 4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        screen.blit(img1, (x * (1400 / 50), y * (700 / 25)))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            board[y][x] = 0
            x += 1
            if x > 48:
                x = 48
            board[y][x] = 1
            for i in board:
                print(i)
            print("-----")
        if keys[pygame.K_LEFT]:
            board[y][x] = 0
            x -= 1
            if x < 0:
                x = 0
            board[y][x] = 1
            for i in board:
                print(i)
            print("-----")
        if keys[pygame.K_UP]:
            board[y][x] = 0
            y -= 1
            if y < 0:
                y = 0
            board[y][x] = 1
            for i in board:
                print(i)
            print("-----")
        if keys[pygame.K_DOWN]:
            board[y][x] = 0
            y += 1
            if y > 21:
                y = 21
            board[y][x] = 1
            for i in board:
               print(i)
            print("-----")
        # if keys[pygame.K_SPACE] and run:
        for i in bomb_list:
            board[i[0]][i[1]] = 4
            screen.blit(img4, (i[1] * (1400 / 50), i[0] * (700 / 25)))
        for i in range(0, 1400, int(700 / 25)):
            for j in range(0, 700, int(1400 / 50)):
                rect = pygame.Rect(i, j, 700 / 25, 1400 / 50)
                pygame.draw.rect(screen, 'black', rect, 1)

        for i in player:
            if i in bomb_list:
                screen.fill('red')

        print(x, y)

        for i in range(y, y + 4):
            for j in range(x, x + 2):
                player.append((i, j))
        for i in player:
            if i in flag:
                screen.fill('green')
        pygame.display.update()
        if keys[pygame.K_SPACE] and run:
            run = False
            time.sleep(0.5)
