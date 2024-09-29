# Write a program that will ask the user for a number that check wether that number is EVEN or ODD

number = int(input("Please enter a number between 1-100:\n"))


# we use the modulus operator % which gives the remainder of the division
# if the number %2 == 0, the number is evenly divisible by 2, meaning its's an even number

if number % 2 == 0:
    print (f"Your user_number {number} is even")

# if number % 2 != 0, the number has a remainder of 1 when divided by 2, meaning it's an odd number 

else:
    print (f"Your user_number {number} is odd") 

