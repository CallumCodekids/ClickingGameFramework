import pygame
from Clickable import Clickable
from SelfModifyingButton import SelfModifyingButton

class SceneSwitchingButton(SelfModifyingButton):
    
    def __init__(self, x, y, width, height, image, thing_to_do, new_scene):
        SelfModifyingButton.__init__(self, x, y, width, height, image, thing_to_do)
        self.new_scene = new_scene
    
    def clicked(self, mousepos, scene):
        was_clicked = Clickable.clicked(self, mousepos, scene)
        if was_clicked:
            self.thing_to_do(self, scene)
        return was_clicked
        