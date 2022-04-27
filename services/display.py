import pandas as pd

class Display: 

    def __init__(self, data, total):
        self.data = data
        self.total = total 

    def view_purchases(self): 
        """Uses Pandas library to display list of items purchased"""
        names = self.data.keys()
        prices = [item['price'] for item in self.data.values()]
        quantities = [item['quantity'] for item in self.data.values()]
        data = pd.DataFrame(data=[names, prices, quantities]).transpose()
        data.columns = ['Item', 'Price', 'Quantity']
        if isinstance(self.total, str): 
            print('==============================================================')
            print(f'           {self.total}')
            print('==============================================================')
        else: 
            print(data)
            print('===============================')
            print(f'        Total:   {self.total}')
            print('===============================')
