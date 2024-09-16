import pygame
from sys import exit
import random
import time
import json

image_filename1 = 'dog.png'
image_filename2 = 'bush.png'
image_filename3 = 'flag.png'
image_filename4 = 'scary_dog.png'
run = True
pygame.init()
width = 1400
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("moving with arrows")
NUM_KEYS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
num = 0
file_read = open("data_base.txt", "r")
save = file_read.read()
print(save.split(":"))
print(type(save.split(":")))
file_read.close()
img1 = pygame.image.load(image_filename1)
img1 = pygame.transform.scale(img1, (2 * (width / 50), 4 * (height / 25)))
img2 = pygame.image.load(image_filename2)
img2 = pygame.transform.scale(img2, (2 * (width / 50), 2 * (height / 25)))
img3 = pygame.image.load(image_filename3)
img3 = pygame.transform.scale(img3, (4 * (width / 50), 3 * (height / 25)))
img4 = pygame.image.load(image_filename4)
img4 = pygame.transform.scale(img4, (3 * (width / 50), 1 * (height / 25)))
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
space_start = 0
player = []
flag = []
for i in range(21, 25):
    for j in range(46, 50):
        flag.append((i, j))

for i in board:
    print(i)

while True:
    screen.fill("dark green")
    screen.blit(img3, (46 * (height / 25), 21 * (width / 50)))
    for i in bush_list:
        board[i[0]][i[1]] = 2
        screen.blit(img2, (i[1] * (width / 50), i[0] * (height / 25)))
    for i in bomb_list:
        board[i[0]][i[1]] = 4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        for i in NUM_KEYS:
            if event.type == pygame.KEYDOWN:  # keydown
                if event.key == i:
                    space_start = pygame.time.get_ticks()
            if event.type == pygame.KEYUP:  # keyup
                if event.key == i:
                    space_end = pygame.time.get_ticks()
                    if space_end - space_start < 1000:
                        data = {
                            "player": (x, y),
                            "bush": bush_list,
                            "bomb": bomb_list,
                            "board": board
                        }
                        file_write = open("data_base.txt", "w")
                        json.dump(data, file_write)
                        file_write.close()
                    else:
                        file_read = open("data_base.txt", "r")
                        base = json.load(file_read)
                        x, y = base["player"][0], base["player"][1]
                        bush_list = base["bush"]
                        bomb_list = base["bomb"]
                        board = base["board"]

        screen.blit(img1, (x * (width / 50), y * (700 / 25)))
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
        if keys[pygame.K_SPACE]:
            screen.fill('black')
            for i in bomb_list:
                board[i[0]][i[1]] = 4
                screen.blit(img4, (i[1] * (width / 50), i[0] * (height / 25)))
            for i in range(0, width, int(height / 25)):
                for j in range(0, 700, int(width / 50)):
                    rect = pygame.Rect(i, j, height / 25, width / 50)
                    pygame.draw.rect(screen, 'green', rect, 1)
            screen.blit(img1, (x * (width / 50), y * (700 / 25)))

        for j in range(x, x + 2):
            player.append((y + 3, j))

        for i in player:
            if i in bomb_list:
                screen.fill('red')
                font = pygame.font.SysFont("Arial", 42)
                txtsurf = font.render("no chicken for you, you dog", True, 'black')
                screen.blit(txtsurf, (470, 280))
                # num += 1

            if i in flag:
                screen.fill('green')
                font = pygame.font.SysFont("Arial", 48)
                txtsurf = font.render("good dog, you can eat today", True, 'black')
                screen.blit(txtsurf, (470, 280))
        pygame.display.update()
        if keys[pygame.K_SPACE]:
            run = False
            time.sleep(0.5)
