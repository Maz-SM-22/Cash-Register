# Cash-Register
## Python cash register CLI app ##

This app calculates the total cost of products ordered based on a product code input and taking into account discounts given set conditions for discounts. The app uses the Pandas library to display the purchased items and the total cost. 

All required packages for this project are listed in `requirements.txt`. 

Tests are included for this application which aim to cover the cases listed in the project specifications and also to test that the discounts are correctly applied. I designed the tests for the project before writing the code, in line with TDD methodology. 

The application can be interactive, taking user input if you run the function in `main.py`. Besides that the main functionality of the program is split into two roles: the cart and the display. The items for purchase are included in a separate config file with the intention that we may be able to add or remove items without touching the cart functions. All available items for purchase are loaded into the cart on This could be extended. 

I have also included descriptive comments for all tests and class functions in order to facilitate reviewing this code and hopefully to eludcidate my thought process in building the app. 

## Points for discusssion ## 
* List input vs. user input - advantages and disadvantages 
* Configuration/externalisation of products and discounts - room for extension 
* Separation of functions in Cart class 
* More extensive testing - coverage of `main.py` and error raising q