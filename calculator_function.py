# first define all the functions with the operation needed
def add (x, y):
    z = x +y
    return z

def subtract (x, y):
    z = x - y
    return z

def multiply (x ,y):
    z = x * y
    return z

def divide (x, y):
    z = x / y
    
    return z

# defining x and y and asking the user to choose any number
x = int(input("choose a number:\t"))
y = int(input("choose a number:\t"))

# calling each of the functions
print (f"The addition of {x} and {y} is:\t{add(x, y)}")

print(f"The subtraction of {x} and {y} is:\t{subtract(x, y)}")

print (f"The multiplication of {x} and {y} is:\t{multiply(x, y)}")

print (f"The division of {x} and {y} is:\t{divide(x, y):.3}")


