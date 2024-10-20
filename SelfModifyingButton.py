import pygame
from Clickable import Clickable
from Button import Button

class SelfModifyingButton(Button):
    
    def clicked(self, mousepos, scene):
        was_clicked = Clickable.clicked(self, mousepos, scene)
        if was_clicked:
            self.thing_to_do(self, scene)
        return was_clicked