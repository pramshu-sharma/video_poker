import pygame
import os
import random


pygame.init()

screen_width, screen_height = 280, 380
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Playing Cards')

cards = os.listdir(os.path.join('cards'))
images = [pygame.image.load(f'cards/{card}') for card in cards]

clock = pygame.time.Clock()
clock.tick(1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            image = images[random.randint(0,51)]

            screen.fill((0, 0, 0))
            screen.blit(image, (75, 70))
            pygame.display.flip()


pygame.quit()
