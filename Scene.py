import pygame

class Scene:
    
    def __init__(self, clickables, displayed,  background_image, event_listeners):
        self.clickables = clickables
        self.displayed = displayed
        self.bg = background_image
        self.event_listeners = event_listeners
        self.event_tracker = {}
        for event in event_listeners:
            self.event_tracker[event] = False
        
    def run(self, screen, clock, fps):
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.running = True
        self.bg = pygame.transform.scale(self.bg,(screen.get_width(),screen.get_height()))
        while self.running:
            for event in self.event_tracker:
                self.event_tracker[event] = False
            for event in pygame.event.get():
                if event.type in self.event_tracker:
                    self.event_tracker[event.type] = True 
            for event in self.event_tracker:
                if self.event_tracker[event]:
                    self.event_listeners[event](self)
            screen.blit(self.bg,(0,0))
            for displayable in self.displayed:
                displayable.display(screen)
            pygame.display.flip()
            clock.tick(fps) 