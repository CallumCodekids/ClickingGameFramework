import pygame
class Clickable:
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.recalculate_rect()
        
    def clicked(self, mouse_pos, scene):
        return self.clickable_rect.collidepoint(mouse_pos)

    def recalculate_rect(self):
        self.clickable_rect = pygame.Rect(self.x, self.y, self.width, self.height)