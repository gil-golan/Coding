import pygame
screen = pygame.display.set_mode((640, 480))

running = True
x = 5
g = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle(screen, (0, g, 0), (320, 240), 50)
    pygame.display.update()
    g += x
    if g>=255 or g<=0:
        x=x*-1





pygame.quit()
