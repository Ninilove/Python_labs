# Write a Python program that prints the largest and smallest values in a list
# Print the two values on the same line, separated by a space
# The largest value should appear first and the smallest value appear second
# You may assume that the list only contains numeric values
# If the list is empty, print None

# Expected output
# list              Output
# [3,4,5,6]           6 3
# [-1,-2,-3,-4]      -1 -4
# [0,0,0,0]           0 0
# []                  []


# List 1
# First we define the list and assign the different items in it
my_list = [3,4,5,6]

# using the if statement with the max and min built-in functions for my_list 1 and 2
if my_list:
    print (max(my_list), min(my_list))
    
else:
    print (my_list, "None")
    
# List 2    
my_list = [-1,-2,-3,-4]
if my_list:
    print (max(my_list), min(my_list))
    
else:
    print (my_list, "None")

# List 3
# On this example, i'm trying the index method to fetch the max and min num (I know they're all zero's but wanted to see the outcome)

my_list = [0,0,0,0]
if my_list:
    print (my_list[0], my_list[3])
    
else:
    print (my_list, "None")    
    
# List 4    
my_list = []

if my_list:
    print (max(my_list), min(my_list))
    
else:
    print ([])



