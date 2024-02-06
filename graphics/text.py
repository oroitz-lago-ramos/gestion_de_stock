import graphics
import pygame

class Text:
    def __init__(self):
        pygame.font.init()
    def draw_center(self, screen, text, x, y ,size=20,color=(0,0,0)):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)
    def draw(self, screen, text, x, y, size=20, color=(0,0,0)):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x,y))
        
    