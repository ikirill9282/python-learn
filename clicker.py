from curses import KEY_UP
from pickle import TRUE
import pygame_widgets
from pygame_widgets.button import Button
import pygame
import time

pygame.init()
win = pygame.display.set_mode((500, 500))  # размеры X и Y
pygame.display.set_caption("Clicker")

bg = pygame.image.load('bg.jpg')
player = pygame.image.load('idle.png')
pygame.display.set_icon(pygame.image.load("idle.bmp"))

x = 0
speed = 1

font = pygame.font.Font("Roboto-Light.ttf", 32)

button = Button(
    # Mandatory Parameters
    win,  # Surface to place button on
    100,  # X-coordinate of top left corner
    100,  # Y-coordinate of top left corner
    300,  # Width
    150,  # Height

    # Optional Parameters
    text='Hello',  # Text to display
    fontSize=50,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    # Colour of button when not being interacted with
    inactiveColour=(200, 50, 0),
    hoverColour=(150, 0, 0),  # Colour of button when being hovered over
    pressedColour=(0, 200, 20),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: print('Click')  # Function to call when clicked on
)

textpos = (10, 10)

clock = pygame.time.Clock()

run = True
while(run):
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка: ", event.button)
            x += speed

    keys = pygame.key.get_pressed()

    if x > 10:
        pygame_widgets.update(event)
        x += speed
        time.sleep(1)
    if keys[pygame.K_TAB]:
        x = 0
    if keys[pygame.K_ESCAPE]:
        run = False

    win.blit(bg, (0, 0))
    win.blit(player, (230, 230))
    text = font.render(str(x), True, [255, 255, 255])
    win.blit(text, textpos)
    pygame.display.update()

pygame.quit()
