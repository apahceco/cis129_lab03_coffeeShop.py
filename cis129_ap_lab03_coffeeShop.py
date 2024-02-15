'''
#  Author: Anthony Pacheco 
#  Class: CIS 129 
#  Project_Name: cis129_lab03_coffeeShop.py
#  Description: This program will demonstrate a coffee shop interaction. 
The user will be asked how many coffees and muffins they want to order and display a recipe. 
The recipe will display the amount of coffee and muffins ordered and the price of each with 
additional sales tax for the total amount due. 
# Version: 1
'''
# Greeting
print('Hi, welcome to BA Coffee and Muffin Shop!\n\nOur cups of coffee are 5 US dollars and are muffins are 4 US dollars.\n\nAt the end of your order, there will be an included 6 percent tax on your subtotal.\n') 


num_coffees = int(input("How many cups of coffee would you like to order.\n")) # Promps the user for how many coffees and adds a new line for better readability.
price_coffees = 5 * num_coffees  # This will process the number of coffees and multiply it by the price for the receipt. 


num_muffins = int(input("How many muffins would you like to order.\n")) # Promps the user for how many muffins and adds a new line for better readability.
price_muffins = 4 * num_muffins # This will process the number of muffins and multiply it by the price for the receipt. 

print('\n') # To add space between the the receipt. 

tax = (price_coffees + price_muffins) * .06  # This will process the tax amount. 
grand_total = price_coffees + price_muffins + tax # This will process total amount. 

# Lines 28-40 are for the receipt. 
print('Thank you for your order today!\nHere is your receipt!')
print('\n')
print('***********************************\nBA Coffee and Muffin Shop\nNumber of coffees bought?')
print(num_coffees) # Line 15
print('Number of muffins bought?')
print(num_muffins) # Line 19
print('***********************************\n***********************************\nBA Coffee and Muffins Shop Receipt')
print(num_coffees,'Coffee\'s at $5 each: $',price_coffees) # Line 15,16
print(num_muffins,'Muffins at $4 each: $',price_muffins) # Line 19,20
print('6% tax:$',tax) # Line 24
print('----------')
print('Total:$',grand_total) # Line 25 
print('***********************************')

print('\n') # Extra spacing
# Farewell 
print('Have a fantastic day!\nSee you next time!')
