# write a code using functions that will add items in your grocery cart and return total in a receipt text

order = {'tomato':30, 'thyme':4.50, 'garlic':7.5, 'rice':10, 'onions':4, 'fish':9.99}

# define a function to add items to the cart and calculate the total
def add_to_cart (cart_items):
    total_cost = sum (cart_items.values()) # the built-in method values is going to retrieve all values from the dictionary without the key
    return total_cost

# define a function to create the receipt
def generate_receipt (cart_items, total):
    with open ('receipt.txt' ,'w') as file: # this will create a file called receipt.txt where 
        file.write ("----Grocery Receipt----\n") # the tile of our receipt
        for item, price in cart_items.items():
# the capitalize built-in method is going to capitalize the first letters of each item in the list and 
            file.write(f'{item.capitalize()}: ${price:.2f}\n')
        file.write ("-------------------------\n")
        file.write (f"Total; ${total:.2f}\n")
        file.write ("-------------------------\n")
    
    print ("Receipt Generated: receipt.txt")

# calculate the total and generate receipt    
total = add_to_cart(order)
generate_receipt (order, total)