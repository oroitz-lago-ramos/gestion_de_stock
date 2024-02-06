# Class button where I can get_coords and draw the button.
# Get coords is a method that returns the coordinates of the button in order to check if the mouse is over the button in another module.
import graphics
import pygame

class Button:
    def __init__(self, x, y, width, height, text, action) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 3)
        graphics.Text().draw_center(screen, self.text, self.rect.centerx, self.rect.centery)

    def handle_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()