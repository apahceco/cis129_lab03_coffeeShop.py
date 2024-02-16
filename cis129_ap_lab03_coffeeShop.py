'''
#  Author: Anthony Pacheco 
#  Class: CIS 129 
#  Project_Name: cis129_lab03_coffeeShop.py
#  Description: This program will demonstrate a coffee shop interaction. 
The user will be asked how many coffees, espressos, muffins, and bagels the user wants to order and display a recipe. 
The recipe will display the amount of coffees, espressos, muffins, and bagels ordered with the price of each and the  
additional sales tax for the total amount due. 
# Version: 2
'''
# Line 11 is Greeting, menu. 
print('Hi, welcome to BA Coffee and Muffin Shop!\n\nOur Menu\n\nCup of Coffee:$5\nShot of Espresso:$8\nMuffins:$4\nBagels:$5\n\nAt the end of your order, there will be an included 6 percent tax on your subtotal.\n') 
print('When you\'re ready, please enter a whole digit number.\nEx:1,12,100\n') # With directions to enter a whole number in digit format with example. 

num_coffees = int(input("How many cups of coffee would you like to order?\n")) # Promps the user for how many coffees and adds a new line for better readability.
price_coffees = 5 * num_coffees  # This will process the number of coffees and multiply it by the price for the receipt. 

num_espresso = int(input("How many shots of espresso would you like to order?\n")) # Promps the user for how many shots of espresso and adds a new line for better readability.
price_espresso = 8 * num_espresso # This will process the number of espresso shots and multiply it by the price for the receipt. 

num_muffins = int(input("How many muffins would you like to order?\n")) # Promps the user for how many muffins and adds a new line for better readability.
price_muffins = 4 * num_muffins # This will process the number of muffins and multiply it by the price for the receipt. 

num_bagels = int(input("How many bagels would you like to order?\n")) # Promps the user for how many bagels and adds a new line for better readability.
price_bagels = 5 * num_bagels # This will process the number of bagels and multiply it by the price for the receipt. 

print('\n') # To add space between the the receipt. 

tax = (price_coffees + price_espresso + price_muffins + price_bagels) * .06  # This will process the tax amount. 
grand_total = price_coffees + price_espresso + price_muffins + price_bagels + tax # This will process total amount. 

# Lines 32-48 are for the receipt. 
print('Thank you for your order today!\nHere is your receipt!')
print('\n')
print('***********************************\n\nBA Coffee and Muffin Shop')
print('Number of coffees bought?\n',num_coffees) # Line 15
print('Number of espresso bought?\n',num_espresso) # Line 18
print('Number of muffins bought?\n',num_coffees) # Line 21
print('Number of bagels bought?\n',num_bagels) # Line 24
print('***********************************\n\n***********************************\n\nBA Coffee and Muffins Shop Receipt')
print(num_coffees,'Coffee\'s at $5 each: $',price_coffees) # Line 15,16
print(num_espresso,'Espresso\'s at $8 each: $',price_espresso) # Line 18,19
print(num_muffins,'Muffins at $4 each: $',price_muffins) # Line 21,22
print(num_bagels,'Bagels\'s at $5 each: $',price_bagels) # Line 24,25
print('6% tax:$',tax) # Line 29
print('----------')
print('Total:$',grand_total) # Line 30 
print('***********************************')

print('\n') # Extra spacing
# Farewell 
print('Have a fantastic day!\nSee you next time!')
