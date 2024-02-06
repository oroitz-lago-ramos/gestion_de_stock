import pygame
import graphics

class Interface:
    def __init__(self,display, button_action):
        self.display = display
        self.screen = self.display.get_screen()
        self.button_action = button_action
        
        self.buttons = [
            graphics.Button(65, 580, 180, 50, "Ajouter un produit", self.button_action.add_product_action),
            graphics.Button(self.display.width // 3 + 65, 580, 180, 50, "Supprimer un produit", self.button_action.delete_product_action),
            graphics.Button(2 * self.display.width // 3 + 65, 580, 180, 50, "Modifier un produit", self.button_action.modify_product_action),
            graphics.Button(730, 15, 150, 50, "Trier par ID", self.button_action.sort_by_id_action),
            graphics.Button(730, 75, 150, 50, "Trier par Nom", self.button_action.sort_by_name_action),
            graphics.Button(730, 135, 150, 50, "Trier par Prix", self.button_action.sort_by_price_action),
            graphics.Button(730, 195, 150, 50, "Trier par Quantité", self.button_action.sort_by_quantity_action),
            graphics.Button(730, 255, 150, 50, "Trier par Catégorie", self.button_action.sort_by_category_action),
        ]
        
    def draw(self):
        product_list_rect = pygame.Rect(5, 5, 700, 550)
        pygame.draw.rect(self.screen, (0, 0, 0), product_list_rect, 3)
        
        control_rect = pygame.Rect(715, 5, 180, 550)
        pygame.draw.rect(self.screen, (0, 0, 0), control_rect, 3)
        
        # Buttons pour ajouter supprimer et modifier des produits qui seront en bas du rectangle de la liste en horizontal
        for button in self.buttons:
            button.draw(self.display.screen)
            
    
    