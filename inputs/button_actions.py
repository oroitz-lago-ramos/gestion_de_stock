import app

class Button_actions:
    def __init__(self, product) -> None:
        self.categories = app.Category()
        self.product = product
        
    
    def add_product_action(self):
        print("Add new product")
    
    def delete_product_action(self):
        print("delete product")
    
    def modify_product_action(self):
        print("modify product")
    
    def sort_by_id_action(self):
        print("sort by id")
        self.product.products_list = self.product.get_products()
        # self.products.sort_by_id()
    
    def sort_by_name_action(self):
        print("sort by name")
        self.product.products_list = self.product.get_products_ordered_by_name_asc()
        # self.products.sort_by_name()
    
    def sort_by_price_action(self):
        print("sort by price")
        self.product.products_list = self.product.get_products_ordered_by_price_asc()
    
    def sort_by_quantity_action(self):
        print("sort by quantity")
        self.product.products_list = self.product.get_products_ordered_by_quantity_asc()
    
    def sort_by_category_action(self):
        print("sort by category")
        self.product.products_list = self.product.get_products_ordered_by_category_asc()
        