import pygame
from Clickable import Clickable 

class Button(Clickable):
    
    def __init__(self, x, y, width, height, image, thing_to_do):
        Clickable.__init__(self, x, y, width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.thing_to_do = thing_to_do
        
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
    def clicked(self, mousepos, scene):
        was_clicked = Clickable.clicked(self, mousepos)
        if was_clicked:
            self.thing_to_do()
        return was_clicked
        