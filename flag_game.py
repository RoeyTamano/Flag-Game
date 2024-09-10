image_filename = 'pixil-frame-0.png'
image_filename1 = 'dog.png'
import pygame

from sys import exit

pygame.init()
screen = pygame.display.set_mode((1400, 700))
pygame.display.set_caption("moving with arrows")
img = pygame.image.load(image_filename)
img = pygame.transform.scale(img, (500, 500))
img1 = pygame.image.load(image_filename1)
img1 = pygame.transform.scale(img1, (200, 200))
x = 0
y = 0
x1 = 50
y1 = 50
board = [[0 for i in range(50)] for j in range(25)]
board[0][0] = 1
for i in board:
    print(i)
block = 980000 / 1250

while True:
    screen.fill((255, 255, 255))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    screen.blit(img1, (i * (700 / 25), j * (1400 / 50)))
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_RIGHT]:
                x = x + 1
                board[0][x - 1] = 0
                board[0][x] = 1
                for i in board:
                    print(i)
                print("-----------------")
            if keys[pygame.K_LEFT]:
                x = x - 1
                board[0][x + 1] = 0
                board[0][x] = 1
            if keys[pygame.K_UP]:
                y = y - 5
            if keys[pygame.K_DOWN]:
                y = y + 5
            pygame.display.update()
