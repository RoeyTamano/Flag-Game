image_filename = 'pixil-frame-0.png'
image_filename1 = 'dog.png'
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Moving with arrows")
img = pygame.image.load(image_filename)
img = pygame.transform.scale(img, (500, 500))
img1 = pygame.image.load(image_filename1)
img1 = pygame.transform.scale(img1, (200, 200))
x = 0
y = 0
x1 = 50
y1 = 50
while True:
    screen.fill((255, 255, 255))
    screen.blit(img, (x, y))
    screen.blit(img1, (x1, y1))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x = x + 5
    if keys[pygame.K_LEFT]:
        x = x - 5
    if keys[pygame.K_UP]:
        y = y - 5
    if keys[pygame.K_DOWN]:
        y = y + 5
    if keys[pygame.K_w]:
        y1 = y1 - 5
    if keys[pygame.K_s]:
        y1 = y1 + 5
    if keys[pygame.K_a]:
        x1 = x1 - 5
    if keys[pygame.K_d]:
        x1 = x1 + 5
    pygame.display.update()