import data

class Category:
    def __init__(self):
        self.db = data.Database()
        
    def get_category_name(self, id):
        query = f'SELECT * FROM category WHERE id=%s'
        params = (id,)
        return self.db.fetch(query, params)[0][1]