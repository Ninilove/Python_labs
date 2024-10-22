# Write a program that will ask the user for a number that check wether that number is EVEN or ODD

# defining the function and setting the conditions

def check_number (x):
    if x % 2 == 0:
        print (f"Your user number {x} is even")
        
    else:
        print (f"Your user number {x} is odd")
        
    return x
# prompt the user to say enter a number        
number = int (input("Please enter a number between 1-100: \t"))

# calling the function
check_number(number)

        