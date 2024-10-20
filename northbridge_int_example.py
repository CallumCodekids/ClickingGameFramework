import pygame

screen = pygame.display.set_mode((800, 400))
fps = 144
running = True
clock = pygame.time.Clock()
bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg,(screen.get_width(),screen.get_height()))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(bg,(0,0))
    pygame.display.flip()
    clock.tick(fps)
    
pygame.quit()