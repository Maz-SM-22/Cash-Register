from services.cart import Cart
from services.display import Display

def run_cash_register(): 
    cart = Cart([]) 
    while cart.open: 
        item = input('Please enter an item code or enter "DONE" to finish shopping: ')
        if item == 'DONE': 
            cart.calculate_total()
            cart.close()
        elif item not in cart.products: 
            print('That item does not exist')
        else: 
            cart.items.append(item)
    return cart.total 

run_cash_register()