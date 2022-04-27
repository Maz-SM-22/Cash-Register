from services.cart import Cart
from services.display import Display

def run_cash_register(cart=Cart([])): 
    """A basic function which allows users to enter products and raises an error if the product is not found"""
    while cart.open: 
        item = input('Please enter an item code or enter "DONE" to finish shopping: ')
        if item == 'DONE': 
            purchases = cart.get_items()
            cost = cart.calculate_total()
            cart.close()
        elif item not in cart.products: 
            raise ValueError(f'Item {item} does not exist. Please check your order again')
        else: 
            cart.items.append(item)
    receipt = Display(purchases, cost)
    return receipt.view_purchases()

run_cash_register()