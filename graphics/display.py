import pygame
import graphics
import app
import inputs

class Display:
    def __init__(self,game):
        self.game = game
        self.text = graphics.Text()
        self.width = 900
        self.height = 650
        self.title = "Gestion de Stock"
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        
        self.product = game.product
        self.category = game.category
        
        self.button_action = inputs.Button_actions(self.product)
        self.list = graphics.List(self)
        self.interface = graphics.Interface(self, self.button_action)
    
    def get_screen(self):
        return self.screen
    def quit(self):
        pygame.quit()
    
    def update(self):
        pygame.display.update()
    def fill(self, color):
        self.screen.fill(color)
    
    def draw_main(self):
        self.fill((255, 255, 255))
        # graphics.Text().draw(self.screen, "Gestion de Stock", self.width / 2, 30, 50)
        
        self.interface.draw()
        self.list.draw()
        
        self.update()
    