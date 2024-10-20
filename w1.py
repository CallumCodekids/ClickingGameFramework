import pygame
from Clickable import Clickable
from Button import Button
from SelfModifyingButton import SelfModifyingButton

def b1(button):
    button.image = pygame.transform.rotate(button.image, 5)

def b2(button):
    button.y = button.y - 50
    button.recalculate_rect()
    
def b2(button):
    button.y = button.y - 50
    button.recalculate_rect()
    
def main_menu_click_detected(scene):
    m_pos = pygame.mouse.get_pos()
    print(m_pos)
    for click in scene.clickables:
        if click.clicked(m_pos):
            print("A clickable was clicked on")
    

clickables = [Clickable(540,250,40,40)]
buttons = [SelfModifyingButton(400, 200, 100, 250,"bob_the_destroyer.jpg", b1),
           SelfModifyingButton(284, 365, 101, 102,"tap.png",b2)]
screen = pygame.display.set_mode((800, 400))
fps = 144
running = True
clock = pygame.time.Clock()
bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg,(screen.get_width(),screen.get_height()))
while running:
    clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
    if clicked:
        m_pos = pygame.mouse.get_pos()
        print(m_pos)
        for click in clickables + buttons:
            if click.clicked(m_pos):
                print("A clickable was clicked on")
    screen.blit(bg,(0,0))
    for button in buttons:
        button.display(screen)
    pygame.display.flip()
    clock.tick(fps)
    
pygame.quit()