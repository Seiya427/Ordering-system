import sqlite3 as s



class Menu():

    def __init__(self, name):
        self.name = name
        connect = s.connect(r"C:\Users\suriy\OneDrive\Desktop\Code\Ordering system\menu.db")
        cursor = connect.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {name}")
        cursor.execute(f'''CREATE TABLE {name}
               (Item, Price, Type, Allergies)''')
    
    def addItem(self, item : str, price : float, Type : str, allergies = ''):
        connect = s.connect(r"C:\Users\suriy\OneDrive\Desktop\Code\Ordering system\menu.db")
        cursor = connect.cursor()
        record = f'''INSERT INTO {self.name} VALUES ("{item}", {price}, "{Type}", "{allergies}")'''
        cursor.execute(record)

class Orders():

    def __init__(self):
        connect = s.connect(r"C:\Users\suriy\OneDrive\Desktop\Code\Ordering system\order.db")
        cursor = connect.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS order")
        cursor.execute(f'''CREATE TABLE order
               ()''')
        
class User():

    def __init(self, name, allergies = []):
        self.name = name
        self.spending = 0
        self.allergies = allergies
    
    
mainMenu = Menu("Menu")
mainMenu.addItem('Samosa', 5.2)