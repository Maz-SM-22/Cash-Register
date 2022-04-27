import pytest
import unittest
from services.cart import Cart

class RegisterTest(unittest.TestCase): 

    def test_empty_cart(self): 
        """Check if cart is initiated with no items"""
        empty_cart = Cart([])
        self.assertEqual(len(empty_cart.items), 0)

    def test_CEOs_order(self):
        """Check Buy One Get One Free discount is applied to Green Tea and items' total is correct"""
        CEO_cart = Cart(['GR1', 'GR1'])
        self.assertEqual(CEO_cart.calculate_total(), 3.11)

    def test_COOs_order(self): 
        """Check 50c discount is applied to strawberries and items' total is correct"""
        COO_cart = Cart(['SR1', 'SR1', 'GR1', 'SR1'])
        self.assertEqual(COO_cart.calculate_total(), 16.61)

    def test_VPs_order(self): 
        """Check coffees are 2/3 of original price and that items' total is correct"""
        VP_cart = Cart(['GR1', 'CF1', 'SR1', 'CF1', 'CF1'])
        self.assertEqual(VP_cart.calculate_total(), 30.57)

    def test_bogoff_discount(self): 
        """Check Buy One Get One Free discount is only applied when appropriate"""
        bogoff_cart = Cart(['GR1', 'GR1', 'GR1'])
        self.assertEqual(bogoff_cart.calculate_total(), 6.22)

    def test_strawberries_discount(self): 
        """Check 50c discount is only applied when appropriate"""
        strawberries_cart = Cart(['SR1', 'SR1'])
        self.assertEqual(strawberries_cart.calculate_total(), 10.0)

    def test_coffee_discount(self): 
        """Check coffees are only 2/3 of original price when appropriate"""
        coffee_cart = Cart(['CF1', 'CF1'])
        self.assertEqual(coffee_cart.calculate_total(), 22.46)

    def test_order_irrelevant(self): 
        """Check to make sure the total is the same no matter what the order the items appear in"""
        jumbled_VP_cart = Cart(['CF1', 'SR1', 'CF1', 'GR1', 'CF1'])
        self.assertEqual(jumbled_VP_cart.calculate_total(), 30.57)