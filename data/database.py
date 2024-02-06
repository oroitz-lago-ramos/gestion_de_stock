import mysql.connector

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "root"
        self.database = "store"
    
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="store"
        )
        self.cursor = self.connection.cursor()
    
    def disconnect(self):
        self.connection.close()
        self.cursor.close()
    
    def execute(self, query, values=None):
        self.connect()
        self.cursor.execute(query, values or ())
        self.connection.commit()
        self.disconnect()
        
    def fetch(self, query, values=None):
        self.connect()
        self.cursor.execute(query, values or ())
        result = self.cursor.fetchall()
        self.disconnect()
        return result
        