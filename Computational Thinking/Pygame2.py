import pygame

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
w1 = 2
w_dir1 = 1
w2 = 2
w_dir2 = 2
w3 = 2
w_dir3 = 3
w4 = 2
w_dir4 = 4
w5 = 2
w_dir5 = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (300, 250), w1)
    pygame.draw.circle(screen, (255, 255, 255), (400, 250), w2)
    pygame.draw.circle(screen, (255, 255, 255), (500, 250), w3)
    pygame.draw.circle(screen, (255, 255, 255), (600, 250), w4)
    pygame.draw.circle(screen, (255, 255, 255), (700, 250), w5)
    pygame.display.update()

    w1 += w_dir1
    if w1 >= 50 or w1 <= 2:
        w_dir1 = w_dir1 * -1

    w2 += w_dir2
    if w2 >= 50 or w2 <= 2:
        w_dir2 = w_dir2 * -1

    w3 += w_dir3
    if w3 >= 50 or w3 <= 2:
        w_dir3 = w_dir3 * -1

    w4 += w_dir4
    if w4 >= 50 or w4 <= 2:
        w_dir4 = w_dir4 * -1

    w5 += w_dir5
    if w5 >= 50 or w5 <= 2:
        w_dir5 = w_dir5 * -1

    clock.tick(100)
pygame.quit()
