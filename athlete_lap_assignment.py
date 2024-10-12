# write a Python program that uses a list of four U.S women athletes who have competed in the 400 meters at the Olympics with the following
# create a list called athletes 

athletes =["Allison Felix", "Sanya Richards-Ross", "Shaunae Miller-Uibo", "Phyllis Francis"]

# Initialize the lap counter starting at 0. When I did 1 it did not work
lap = 0

# use a for loop to display each athlete's name along with lap number they have completed.

for athlete in athletes:
    lap += 1 # using the count method
    print (f"Lap {lap}: {athlete} has completed their lap!")

# print the end message    
print ("\n All athletes have completed their laps!")

    

    
    
