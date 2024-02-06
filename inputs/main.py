import pygame

class Input:
    def __init__(self,game, display):
        self.game = game
        self.display = display
        self.interface = display.interface
        
    
    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.is_running = False
            for button in self.interface.buttons:
                button.handle_click(event)