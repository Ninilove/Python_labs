# Lab cake 2: Reversing a list
# Objective: Practice reversing a list and transferring its elements into a new list using loops
# Task: Write a Python program that works with a list called laura_things containing the following items: sewing machine, scissor, cutting mat, television
# Your program should do the following


# 1- create a list called laura_things with the items listed above

laura_things = ["sewing machine", "scissor", "cutting mat", "television"]
print (f"The original order from the laura_things list is:\t {laura_things}\n")

for index in range(len(laura_things)):
    print (f"Item {index +1} in the list is {laura_things[index]} and is at index: {index}") # trying to replicate what we did in class
# 2- reverse the order of the list in laura_things using the loop method

# 3-4- Empty list to store reversed items and transfer each item from the list into a new list called reversed_things

reversed_things = []
# Loop through the original list in reverse order and append each item
for reverse_list in range(len(laura_things)):
    reversed_things.append(laura_things [::-1][reverse_list])
    
print(f" \nThe reversed order from the laura_things list is:\t {reversed_things}\n")

# using the slicing method    
#reverse_things = (laura_things[::-1])
#print (f"The reverse order from the laura_things list is:\t {reverse_things}")

print (f" \nThe final output of laura_things list in reversed order is:\n {reversed_things}\n") 

for index in range(len(laura_things)):
    
    print (f"Item {index +1} in the reversed list is {reversed_things[index]} and is at index: {index}") # trying to replicate what we did in class
    
# 5- Print a message that says 'The list has been successfully reversed!

print("\nThe list has been successfully reversed!")
