import pygame
import random
screen = pygame.display.set_mode((1000, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(300, 30, -10):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        pygame.draw.circle(screen, (a, b, c), (500, 300), i)
        pygame.draw.circle(screen, (0, 0, 0), (500, 300), i-10)
        pygame.display.update()
pygame.quit()