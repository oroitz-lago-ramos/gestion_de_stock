import graphics

class List:
    def __init__(self, display):
        self.display = display
    
    def draw(self):
        products = self.display.game.product.products_list
        start_y = 15  # Starting y-coordinate, adjust as needed
        start_x = 15  # Starting x-coordinate, adjust as needed
        y_spacing = 20  # Vertical spacing between rows, adjust as needed
        column_spacings = [20, 200, 250, 50]  # Horizontal spacing for each column, adjust as needed
        default_spacing = 50
        
        y = start_y
        for i, product in enumerate(products):
            x = start_x
            for j, element in enumerate(product):
                if j == 5:
                    element = self.display.game.category.get_category_name(element)
                graphics.Text().draw(self.display.screen, str(element), x, y)
                x += column_spacings[j] if j < len(column_spacings) else default_spacing
            y += y_spacing  # Move y-coordinate down for the next row
        
        
        # for i, product in enumerate(products):
        #     id = str(product[0])
        #     name = product[1]
        #     price = product[3]
        #     quantity = product[4]
        #     category = self.display.game.category.get_category_name(product[5])
        #     description = product[2]
        #     print(id, name, description, price, quantity, category)
            