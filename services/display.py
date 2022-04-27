import pandas as pd

class Display: 

    def __init__(self, data, total):
        self.data = data
        self.total = total 

    def view_purchases(self): 
        names = self.data.keys()
        prices = [item['price'] for item in self.data.values()]
        quantities = [item['quantity'] for item in self.data.values()]
        data = pd.DataFrame(data=[names, prices, quantities]).transpose()
        data.columns = ['Item', 'Price', 'Quantity']
        print(data)
        print('===============================')
        print(f'           Total: {self.total}')
        print('===============================')
