import os 
import json
import math  
from itertools import groupby

class Cart: 

    def __init__(self, items):
        self.open = True 
        self.total = 'You currently have no items in your basket'
        self.items = items 
        self.products = self.get_products()

    def close(self): 
        """Set the status of the cart to keep it open while completing purchases"""
        self.open = False 

    def get_products(self): 
        """Load external file with listed items available for purchase in"""
        project_root = os.getenv('PYTHONPATH')
        with open(f'{project_root}/products/products.json') as stock_file: 
            stock = json.load(stock_file)
            return stock['products']

    def get_items(self):
        """Converts individually listed items into list with all items, their price and quantity purchased"""
        items = []
        for item in sorted(self.items): 
            items.append(self.products[item])
        grouped = {}
        for name, article in groupby(items, key=lambda item: item["name"]):
            products = list(article)
            grouped[name] = {
                "price": products[0]["price"],
                "quantity": len(products),
            }
        return grouped

    def calculate_total(self):
        """Uses the previous function to apply discounts and calculate total"""
        self.items = self.get_items()
        if len(self.items) == 0: 
            return self.total 
        else:             
            self.total = 0 
            for item in self.items: 
                if item == 'Green Tea' and self.items[item]['quantity'] > 1:
                    self.total += self.items[item]['price'] * math.ceil(self.items[item]['quantity'] / 2)
                elif item == 'Strawberries' and self.items[item]['quantity'] >= 3: 
                    self.items[item]['price'] = 4.50
                    self.total += self.items[item]['price'] * self.items[item]['quantity']
                elif item == 'Coffee' and self.items[item]['quantity'] >= 3: 
                    self.items[item]['price'] = self.items[item]['price'] * (2 / 3) 
                    self.total += round(self.items[item]['price'] * self.items[item]['quantity'], 2)
                else: 
                    self.total += self.items[item]['price'] * self.items[item]['quantity']
        return self.total
