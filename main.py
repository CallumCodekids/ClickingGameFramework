import pygame
from Clickable import Clickable
from Button import Button
from SelfModifyingButton import SelfModifyingButton
from SceneSwitchingButton import SceneSwitchingButton

from Scene import Scene

def b1(button, scene):
    button.image = pygame.transform.rotate(button.image, 5)

def b2(button, scene):
    button.y = button.y - 50
    button.recalculate_rect()
    
def b2(button, scene):
    button.y = button.y - 50
    button.recalculate_rect()
    
def switch_scence(button, scene):
    button.running = False
    button.new_scene.run(scene.screen, scene.clock, scene.fps)
    
def main_menu_click_detected(scene):
    m_pos = pygame.mouse.get_pos()
    print(m_pos)
    for click in scene.clickables:
        if click.clicked(m_pos):
            print("A clickable was clicked on")
            

def quit_scene(scene):
    scene.running = False
    
def check_clickables(scene):
    m_pos = pygame.mouse.get_pos()
    print(m_pos)
    for click in scene.clickables:
        if click.clicked(m_pos, scene):
            print("A clickable was clicked on")
            

    

clickables = [Clickable(540,250,40,40)]
screen = pygame.display.set_mode((800, 400))

listeners = {pygame.QUIT:quit_scene, pygame.MOUSEBUTTONDOWN: check_clickables}


bg2 = pygame.image.load("bg2.gif")
bg2 = pygame.transform.scale(bg2,(screen.get_width(),screen.get_height()))

scene_2 = Scene([],[],bg2, listeners)


buttons = [SelfModifyingButton(400, 200, 100, 250,"bob_the_destroyer.jpg", b1),
           SelfModifyingButton(284, 365, 101, 102,"tap.png",b2),
           SceneSwitchingButton(1,296, 150, 98, "cheese_man_eater.png",switch_scence, scene_2)]


bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg,(screen.get_width(),screen.get_height()))



scene_1 = Scene(clickables + buttons, buttons, bg, listeners)

fps = 144
clock = pygame.time.Clock()


scene_1.run(screen, clock, fps)
    
pygame.quit()