from pickle import TRUE
import pygame
import time

WIDTH = 500
HEIGHT = 700
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))  # размеры X и Y
pygame.display.set_caption("Move")

bg = pygame.image.load('bg.jpg')
player = pygame.image.load('idle.png')

x = 50
y = 50
speed = 5

font = pygame.font.Font("Roboto-Light.ttf", 32)
text = font.render("Game over!", True, [255, 255, 255])

textpos = (10, 10)

clock = pygame.time.Clock()
run = True
while(run):
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed

    win.blit(bg, (0, 0))
    win.blit(player, (x, y))
    if x <= -1:
        win.blit(text, textpos)
        # run = False
    if y <= -1:
        win.blit(text, textpos)
    pygame.draw.rect(win, (239, 35, 60),
                     (0, 0, WIDTH, 60))
    # win.blit(text, textpos)
    pygame.display.update()

pygame.quit()
