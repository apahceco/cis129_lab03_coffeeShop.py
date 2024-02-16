'''
#  Author: Anthony Pacheco 
#  Class: CIS 129 
#  Project_Name: cis129_lab03_coffeeShop.py
#  Description: This program will demonstrate a coffee shop interaction. 
The user will be asked how many coffees, espressos, muffins, and bagels the user wants to order and display a recipe. 
The recipe will display the amount of coffees, espressos, muffins, and bagels ordered with the price of each and the  
additional sales tax for the total amount due. 
# Version: 3
'''

# Line 11 is Greeting, menu. 
print('Hi, welcome to BA Coffee and Muffin Shop!\n\nOur Menu\n\nCup of Coffee:$5\nShot of Espresso:$8\nMuffins:$4\nBagels:$5\n\nAt the end of your order, there will be an included 6 percent tax on your subtotal.\n') 
print('When you\'re ready, please enter a whole digit number.\nEx:0,4,12,100...\n') # With directions to enter a whole number in digit format with example. 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
numCoffees = int(input("How many cups of coffee would you like to order?\n")) # Promps the user for how many coffees and adds a new line for better readability.
priceCoffees = 5 * numCoffees  # This will process the number of coffees and multiply it by the price for the receipt. 

numEspresso = int(input("How many shots of espresso would you like to order?\n")) # Promps the user for how many shots of espresso and adds a new line for better readability.
priceEspresso = 8 * numEspresso # This will process the number of espresso shots and multiply it by the price for the receipt. 

numMuffins = int(input("How many muffins would you like to order?\n")) # Promps the user for how many muffins and adds a new line for better readability.
priceMuffins = 4 * numMuffins # This will process the number of muffins and multiply it by the price for the receipt. 

numBagels = int(input("How many bagels would you like to order?\n")) # Promps the user for how many bagels and adds a new line for better readability.
priceBagels = 5 * numBagels # This will process the number of bagels and multiply it by the price for the receipt. 

print('\n') # To add space between the the receipt. 

tax = (priceCoffees + priceEspresso + priceMuffins + priceBagels) * .06  # This will process the tax amount. 
grandTotal = priceCoffees + priceEspresso + priceMuffins + priceBagels + tax # This will process total amount. 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Lines 32-48 are for the receipt. 
print('Thank you for your order today!\nHere is your receipt!')
print('\n')
print('***********************************\n\nBA Coffee and Muffin Shop')
print('Number of coffees bought?\n',numCoffees) # Line 15
print('Number of espresso bought?\n',numEspresso) # Line 18
print('Number of muffins bought?\n',numMuffins) # Line 21
print('Number of bagels bought?\n',numBagels) # Line 24
print('***********************************\n\n***********************************\n\nBA Coffee and Muffins Shop Receipt')
print(numCoffees,'Coffee\'s at $5 each: $',priceCoffees) # Line 15,16
print(numEspresso,'Espresso\'s at $8 each: $',priceEspresso) # Line 18,19
print(numMuffins,'Muffins at $4 each: $',priceMuffins) # Line 21,22
print(numBagels,'Bagels\'s at $5 each: $',priceBagels) # Line 24,25
print('6% tax:$',tax) # Line 29
print('----------')
print('Total:$',grandTotal) # Line 30 
print('***********************************')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('\n') # Extra spacing
# Farewell
print('Have a fantastic day!\n\nSee you next time!')
