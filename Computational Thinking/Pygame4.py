import pygame
import random
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 500))

x = random.randint(1, 1000)
y = random.randint(1, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x2 = random.randint(1, 1000)
    y2 = random.randint(1, 500)
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 10)
    pygame.draw.circle(screen, (255, 0, 0), (x2, y2), 10)

    pygame.draw.line(screen, (0, 0, 255), (x2, y2), (x, y), 2)

    x = x2
    y = y2
    clock.tick(10)

    pygame.display.update()

pygame.quit()
