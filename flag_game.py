import pygame
from sys import exit
import random

image_filename1 = 'dog.png'
image_filename2 = 'bush.png'

pygame.init()
screen = pygame.display.set_mode((1400, 700))
pygame.display.set_caption("moving with arrows")

img1 = pygame.image.load(image_filename1)
img1 = pygame.transform.scale(img1, (2 * (700 / 25), 4 * (1400 / 50)))
img2 = pygame.image.load(image_filename2)
img2 = pygame.transform.scale(img2, (2 * (700 / 25), 2 * (1400 / 50)))
x = 0
y = 0

board = [[0 for i in range(50)] for j in range(25)]
for i in range(20):
    random_row = random.randint(0, 24)
    random_col = random.randint(0, 49)
    if board[random_row][random_col] == 0:
        board[random_row][random_col] = 2
board[0][0] = 1

for i in board:
    print(i)

while True:
    screen.fill("dark green")
    for i in range(25):
        for j in range(50):
            if board[i][j] == 2:
                screen.blit(img2, (j * (1400 / 50), i * (700 / 25)))

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

        pygame.display.update()


