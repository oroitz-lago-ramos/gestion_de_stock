import data

class Product:
    def __init__(self):
        self.db = data.Database()
        self.products_list = self.get_products()
        
    def get_products(self):
        return self.db.fetch("SELECT * FROM product")
    
    def get_products_ordered_by_price_desc(self):
        return self.db.fetch("SELECT * FROM product ORDER BY price DESC")
    def get_products_ordered_by_price_asc(self):
        return self.db.fetch("SELECT * FROM product ORDER BY price ASC")
    
    def get_products_ordered_by_name_asc(self):
        return self.db.fetch("SELECT * FROM product ORDER BY name ASC")
    def get_products_ordered_by_name_desc(self):
        return self.db.fetch("SELECT * FROM product ORDER BY name DESC")
    
    def get_products_ordered_by_category_asc(self):
        return self.db.fetch("SELECT * FROM product ORDER BY id_category ASC")
    def get_products_ordered_by_category_desc(self):
        return self.db.fetch("SELECT * FROM product ORDER BY id_category DESC")
    
    def get_products_ordered_by_quantity_asc(self):
        return self.db.fetch("SELECT * FROM product ORDER BY quantity ASC")
    def get_products_ordered_by_quantity_desc(self):
        return self.db.fetch("SELECT * FROM product ORDER BY quantity DESC")
    
    
    
        