# Prompt the user to enter age as in integer

age = int(input("Enter your {age}:\t"))

# using the less than or equal operator to check if the age falls within a certain range

if 0 <= age <= 1 :
    print("You are an infant")
    
elif 2 <= age <= 3 :
    print ("You are a toddler")
    
elif 4 <= age <= 12 :
    print ("You are a child")
    
elif 13 <= age <= 19:
    print ("You are a teenager") 
    
elif 20 <= age <= 64:
    print ("You are an adult")
    
elif 65 <= age <= 130:
    print ("You are a senior")
    
# if none of the ages the user will enter is valid, this message will appear instead
else:
    print ("Invalid age")

        