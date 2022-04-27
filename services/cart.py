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
        self.open = False 

    def get_products(self): 
        with open('../products/products.json') as stock_file: 
            stock = json.load(stock_file)
            return stock['products']

    def get_items(self):
        items = []
        for item in self.items: 
            items.append(self.products[item])
        grouped = {}
        for name, article in groupby(sorted(items), key=lambda item: item["name"]):
            products = list(article)
            grouped[name] = {
                "price": products[0]["price"],
                "quantity": len(products),
            }
        return grouped

    def calculate_total(self):
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

cart = Cart(['SR1', 'SR1', 'SR1', 'GR1', 'CF1', 'GR1'])
print(cart.calculate_total())